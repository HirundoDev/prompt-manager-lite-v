# Schema Playbook: masterBlueprint

Purpose
- Defines the high-level orchestrator that composes all master blueprint parts via $ref to produce a unified project blueprint.

Schema Structure
- $schema: draft-07
- properties: refs to each sub-schema in `schemas/master_blueprint_parts/*`
- definitions: refs `definitions.json#/definitions`

How to Use
1) Complete or update each sub-schema in `master_blueprint_parts/`.
2) Validate the whole blueprint using this schema as the root.
3) Keep $refs stable; do not rename or move files.

Example (snippet)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$comment": "Playbook: prompt_playbooks/schemas_playbooks/playbook_schema-masterBlueprint.md",
  "title": "Master Blueprint for Software Projects V3 (Modular)",
  "properties": {
    "projectInfo": { "$ref": "master_blueprint_parts/projectInfo.json" }
  }
}
```

Checklist
- [ ] All sub-schemas referenced exist and validate
- [ ] $comment present and points to this playbook
- [ ] combine_schemas.py generates master_blueprint_combined.json without errors

Best Practices
- Keep sub-schemas independent and versioned
- Add new modules via new sub-schemas rather than expanding this root excessively
