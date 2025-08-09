#!/usr/bin/env python3
"""
Verificador de Documentación y Schemas

Comprueba:
1) Manifiesto de documentación (manifests/documentation_manifest.json)
   - Campos requeridos por el schema
   - Existencia de cada archivo DOC
2) Cobertura de playbooks de documentación
   - Existe playbook canónico por cada DOC
   - Alias conocidos presentes (sin fallar)
3) Cobertura de schemas en la guía CONEXION_SCHEMAS_DOCS.md
   - Cada schema *.json bajo schemas/ aparece mencionado en la guía
4) Presencia de cada DOC en la guía USO_PLAYBOOKS_DOCS.md (índice DOCs ↔ Playbooks)

No requiere dependencias externas.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Detect repo root even if script is inside tools/
SCRIPT_DIR = Path(__file__).resolve().parent
if (SCRIPT_DIR / 'manifests').exists() and (SCRIPT_DIR / 'guides').exists():
    BASE = SCRIPT_DIR
else:
    BASE = SCRIPT_DIR.parent
DOCS_DIRS = [BASE / "docs", BASE / "real_structure_documentation" / "docs"]
PB_DOCS_DIR = BASE / "prompt_playbooks" / "documentation_playbooks"
SCHEMAS_DIRS = [BASE / "schemas", BASE / "real_structure_documentation" / "schemas"]
GUIDE_CONN = BASE / "guides" / "CONEXION_SCHEMAS_DOCS.md"
GUIDE_PB_DOCS = BASE / "guides" / "USO_PLAYBOOKS_DOCS.md"
MANIFEST_PATH = BASE / "manifests" / "documentation_manifest.json"

ALIASES = {
    "DOC017-ADR-Index": {"playbook-v2-DOC017-ADRIndex.md"},
    "DOC019-CLI-Command-Reference": {"playbook-v2-DOC019-CLICommandReference.md"},
    # Diferencia de capitalización en el repositorio para DOC020
    "DOC020-CodeOfConduct": {"playbook-v2-DOC020-CodeofConduct.md"},
}

CANONICAL_PB_PATTERN = "playbook-v2-{doc_basename}.md"

# Schemas meta que no deben contarse para cobertura por schemaRefs
EXCLUDED_SCHEMA_COVERAGE: Set[str] = {
    "schemas/master_blueprint_schema.json",
    "schemas/master_blueprint_parts/documentationManifest.json",
    "real_structure_documentation/schemas/master_blueprint_schema.json",
    "real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json",
}


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def list_docs() -> List[Path]:
    files: List[Path] = []
    for d in DOCS_DIRS:
        if d.exists():
            files.extend(d.glob("DOC*.md"))
    return sorted(set(files))


def list_playbooks() -> Set[str]:
    if not PB_DOCS_DIR.exists():
        return set()
    return {p.name for p in PB_DOCS_DIR.glob("playbook-v2-*.md")}


def list_schema_files() -> List[Path]:
    files: List[Path] = []
    for d in SCHEMAS_DIRS:
        if d.exists():
            files.extend(d.rglob("*.json"))
    return sorted(set(files))


def check_manifest(manifest: dict, docs_on_disk: List[Path]) -> Tuple[List[str], List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    ok: List[str] = []

    # Index docs by multiple key forms (absolute, relative to BASE, and relative to docs/ and real_structure_documentation/docs)
    docs_by_path: Dict[str, Path] = {}
    for p in docs_on_disk:
        abs_key = str(p.as_posix())
        rel_base = str(p.relative_to(BASE).as_posix())  # e.g., 'docs/DOC000-...'
        rel_docs = f"docs/{p.name}"
        rel_docs2 = f"real_structure_documentation/docs/{p.name}"
        docs_by_path[abs_key] = p
        docs_by_path[rel_base] = p
        docs_by_path[rel_docs] = p
        docs_by_path[rel_docs2] = p

    # Validate structure
    if "documents" not in manifest or not isinstance(manifest["documents"], list):
        errors.append("Manifest: campo 'documents' ausente o inválido")
        return ok, warnings, errors

    # Check each entry
    manifest_paths = set()
    covered_docs: Set[Path] = set()
    for i, d in enumerate(manifest["documents"]):
        missing = [k for k in ("title", "path", "ownerAgent") if k not in d]
        if missing:
            errors.append(f"Manifest.documents[{i}]: faltan campos requeridos: {', '.join(missing)}")
            continue
        status = d.get("status")
        if status and status not in {"draft", "review", "approved"}:
            warnings.append(f"Manifest.documents[{i}]: status '{status}' no está en ['draft','review','approved']")
        path = d["path"]
        manifest_paths.add(path)
        if path not in docs_by_path:
            errors.append(f"Manifest: archivo no existe en disco: {path}")
        else:
            ok.append(f"Manifest OK: {path}")
            covered_docs.add(docs_by_path[path])

        # Soft-check: schemaRefs existence (optional field)
        schema_refs = d.get("schemaRefs", [])
        for sref in schema_refs:
            # Normalizamos: permitir relativos al repo
            sref_path = (BASE / sref).resolve()
            if not sref_path.exists():
                warnings.append(f"Manifest: schemaRef no encontrado: {sref}")

    # Ensure every DOC on disk appears in manifest
    for p in docs_on_disk:
        if p not in covered_docs:
            warnings.append(f"Manifest: DOC en disco no listado: {p.as_posix()}")

    return ok, warnings, errors


def check_playbooks(docs_on_disk: List[Path], pb_names: Set[str]) -> Tuple[List[str], List[str], List[str]]:
    ok: List[str] = []
    warnings: List[str] = []
    errors: List[str] = []

    for doc in docs_on_disk:
        basename = doc.name  # e.g., DOC017-ADR-Index.md
        doc_basename = basename[:-3]  # sin .md
        canonical = CANONICAL_PB_PATTERN.format(doc_basename=doc_basename)

        if canonical in pb_names:
            ok.append(f"Playbook OK: {canonical}")
            continue

        # check aliases
        alias_set = ALIASES.get(doc_basename, set())
        if any(a in pb_names for a in alias_set):
            warnings.append(f"Playbook alias presente para {doc_basename}: {sorted(alias_set)} (falta canónico {canonical})")
        else:
            errors.append(f"Playbook faltante: {canonical}")

    return ok, warnings, errors


def check_schemas_covered_in_guide(schema_files: List[Path], guide_path: Path) -> Tuple[List[str], List[str]]:
    if not guide_path.exists():
        return [], [f"Guía no encontrada: {guide_path}"]
    guide_text = guide_path.read_text(encoding="utf-8")
    ok: List[str] = []
    warnings: List[str] = []
    for s in schema_files:
        # nombres relativos a cada base de schemas/
        rels: Set[str] = set()
        for base_dir in SCHEMAS_DIRS:
            try:
                rels.add(s.relative_to(base_dir).as_posix())
            except ValueError:
                pass
        name = s.name
        mentioned = False
        for rel in rels:
            if (
                name in guide_text
                or f"schemas/{rel}" in guide_text
                or f"real_structure_documentation/schemas/{rel}" in guide_text
            ):
                mentioned = True
                ok.append(f"Schema mencionado en guía: {rel}")
                break
        if not mentioned:
            # report one sample rel for clarity
            sample = next(iter(rels)) if rels else s.name
            warnings.append(f"Schema NO mencionado en guía: {sample}")
    return ok, warnings


def check_schema_refs_coverage(schema_files: List[Path], manifest: dict) -> Tuple[List[str], List[str]]:
    ok: List[str] = []
    warnings: List[str] = []
    # Build a canonical set of rel paths like 'schemas/...' for all schemas on disk.
    # We'll accept either prefix in inputs but normalize to this canonical form for coverage.
    all_rel: Set[str] = set()
    for s in schema_files:
        for base_dir in SCHEMAS_DIRS:
            try:
                rel = s.relative_to(base_dir).as_posix()
                all_rel.add(f"schemas/{rel}")
            except ValueError:
                continue
    all_rel = {p for p in all_rel if p not in EXCLUDED_SCHEMA_COVERAGE}
    # Map schema -> docs that reference it
    refs: Dict[str, List[str]] = {k: [] for k in all_rel}
    for d in manifest.get("documents", []):
        doc_id = d.get("id") or d.get("title") or d.get("path")
        for sref in d.get("schemaRefs", []):
            # normalize any new prefix to the canonical 'schemas/' form
            norm = sref
            if sref.startswith("real_structure_documentation/schemas/"):
                norm = sref.replace("real_structure_documentation/schemas/", "schemas/", 1)
            if norm in refs:
                refs[norm].append(doc_id)
    # Evaluate coverage
    for schema, docs in sorted(refs.items()):
        if docs:
            ok.append(f"Schema referenciado en manifest: {schema} ← {', '.join(docs)}")
        else:
            warnings.append(f"Schema SIN referencia en manifest.schemaRefs: {schema}")
    return ok, warnings


def check_docs_indexed_in_guide(docs_on_disk: List[Path], guide_path: Path) -> Tuple[List[str], List[str]]:
    if not guide_path.exists():
        return [], [f"Guía no encontrada: {guide_path}"]
    text = guide_path.read_text(encoding="utf-8")
    ok: List[str] = []
    warnings: List[str] = []
    for doc in docs_on_disk:
        doc_basename = doc.name[:-3]
        # Presencia del código DOC### en el índice
        code_match = re.search(rf"\b{re.escape(doc_basename.split('-')[0])}\b", text)
        if code_match and doc_basename in text:
            ok.append(f"DOC indexado en guía: {doc_basename}")
        else:
            warnings.append(f"DOC NO indexado claramente en guía: {doc_basename}")
    return ok, warnings


def main() -> int:
    print("=" * 60)
    print("🔎 Verificador de Documentación y Schemas")
    print("=" * 60)

    errors_total: List[str] = []
    warnings_total: List[str] = []

    # 1) Manifest
    if MANIFEST_PATH.exists():
        manifest = load_json(MANIFEST_PATH)
    else:
        manifest = {"documents": []}
        warnings_total.append(f"Manifest no encontrado: {MANIFEST_PATH}")

    docs_on_disk = list_docs()
    pb_names = list_playbooks()
    schemas = list_schema_files()

    ok, warn, err = check_manifest(manifest, docs_on_disk)
    warnings_total.extend(warn)
    errors_total.extend(err)
    print(f"📁 DOCs en disco: {len(docs_on_disk)} | Playbooks: {len(pb_names)} | Schemas: {len(schemas)}")

    # 2) Playbooks
    ok2, warn2, err2 = check_playbooks(docs_on_disk, pb_names)
    warnings_total.extend(warn2)
    errors_total.extend(err2)

    # 3) Schemas en guía de conexión
    ok3, warn3 = check_schemas_covered_in_guide(schemas, GUIDE_CONN)
    warnings_total.extend(warn3)

    # 4) Cobertura de schemaRefs en manifest (opcional, pero recomendado)
    ok3b, warn3b = check_schema_refs_coverage(schemas, manifest)
    warnings_total.extend(warn3b)

    # 5) DOCs en índice de guía playbooks-docs
    ok4, warn4 = check_docs_indexed_in_guide(docs_on_disk, GUIDE_PB_DOCS)
    warnings_total.extend(warn4)

    # Resumen
    print("\n" + "-" * 60)
    print("RESULTADO")
    print(f"❌ Errores: {len(errors_total)}")
    for e in errors_total[:50]:
        print(f"  - {e}")
    if len(errors_total) > 50:
        print("  … (más errores omitidos) …")

    print(f"⚠️  Advertencias: {len(warnings_total)}")
    for w in warnings_total[:50]:
        print(f"  - {w}")
    if len(warnings_total) > 50:
        print("  … (más advertencias omitidas) …")

    exit_code = 1 if errors_total else 0
    print("-" * 60)
    print("✔️  OK" if exit_code == 0 else "❗ Revisión necesaria")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
