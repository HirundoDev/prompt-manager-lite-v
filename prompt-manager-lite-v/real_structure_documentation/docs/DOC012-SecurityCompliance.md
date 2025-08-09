# Plantilla Maestra: Postura de Seguridad y Cumplimiento

> **Propósito:** Centralizar todas las políticas, herramientas y procedimientos relacionados con la seguridad y el cumplimiento normativo del software.
> **Playbook de Referencia:** `playbook-v2-DOC012-SecurityCompliance.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Security Agent):
  - Tu misión es generar este documento a partir del objeto `securityAndCompliance` en el `master_blueprint.json`.
-->

## 1. Manejo de Datos y Privacidad

-   **Clasificación de Datos:** `[securityAndCompliance.dataHandling.dataClassification]`
-   **Medidas de Protección:** `[securityAndCompliance.dataHandling.protectionMeasures]`

## 2. Autenticación y Autorización

-   **Métodos de Autenticación:** `[securityAndCompliance.authentication.methods]`
-   **Modelo de Autorización:** `[securityAndCompliance.authentication.authorizationModel]`

## 3. Gestión de Secretos

-   **Herramienta:** `[securityAndCompliance.secretsManagement.tool]`
-   **Política:** `[securityAndCompliance.secretsManagement.policy]`

## 4. Seguridad de Dependencias

-   **Herramienta de Escaneo:** `[securityAndCompliance.dependencySecurity.scanningTool]`
-   **Proceso:** `[securityAndCompliance.dependencySecurity.remediationProcess]`

## 5. Política de Divulgación de Vulnerabilidades

-   **Instrucciones de Reporte:** `[securityAndCompliance.vulnerabilityDisclosure.reportingInstructions]`
-   **Tiempos de Respuesta:** `[securityAndCompliance.vulnerabilityDisclosure.responseTimeline]`

## 6. Cumplimiento Normativo

-   **Estándares y Regulaciones:**
    -   `[Iterar sobre securityAndCompliance.compliance.standards]`