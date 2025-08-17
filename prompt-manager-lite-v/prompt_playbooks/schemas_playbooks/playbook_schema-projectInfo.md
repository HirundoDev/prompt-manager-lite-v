# Playbook: Universal Project Information Schema Template

## Propósito
Este playbook guía el uso del schema `projectInfo.json` como template universal para documentar información de proyectos. El schema utiliza placeholders `[VARIABLE]` que deben ser reemplazados con información específica del proyecto, permitiendo adaptabilidad a cualquier tipo de proyecto, metodología o dominio.

## Filosofía Template-First
- **Schema como Receptor**: El schema está diseñado para RECIBIR información, no para definirla
- **Placeholders Universales**: Usar `[VARIABLE]` para todos los valores específicos del proyecto
- **Adaptabilidad Total**: Funciona para cualquier tipo de proyecto (software, infraestructura, investigación, etc.)
- **Mejores Prácticas Generales**: Incorpora patrones universales de gestión de proyectos sin prescribir metodologías específicas

**Ubicación del schema:** `schemas/master_blueprint_parts/projectInfo.json`

## Metodología de Implementación 2025

### 1. Basic Info - Fundamentos del Proyecto
```json
{
  "basicInfo": {
    "name": "Project Name",
    "description": "Comprehensive project description (min 20 chars)",
    "version": "1.0.0",
    "status": "Planning|In-Progress|Testing|Deployment|Maintenance",
    "type": "Web-Application|Mobile-App|API|Platform",
    "category": "B2B|B2C|Internal-Tool|Enterprise",
    "repository": {
      "url": "https://github.com/org/project",
      "type": "GitHub",
      "visibility": "Private"
    }
  }
}
```

### 2. Project Charter - Visión y Objetivos
Implementar project charter completo con:
- **Vision Statement:** Qué éxito se ve como
- **Mission Statement:** Cómo lograremos la visión
- **SMART Objectives:** Específicos, medibles, alcanzables, relevantes, con tiempo
- **Scope Definition:** Qué está incluido/excluido
- **Success Criteria:** Métricas claras de éxito

```json
{
  "projectCharter": {
    "vision": "Clear vision statement of project success",
    "objectives": [
      {
        "id": "OBJ-001",
        "description": "Specific objective description",
        "measurable": "How success will be measured",
        "timebound": "Q2 2025",
        "priority": "Critical|High|Medium|Low",
        "owner": "Responsible person"
      }
    ],
    "scope": {
      "included": ["Feature A", "Integration B"],
      "excluded": ["Future enhancement C"],
      "assumptions": ["Key assumptions"],
      "constraints": ["Budget, time, resource constraints"]
    }
  }
}
```

### 3. Stakeholder Management - Mapeo Completo
Identificar y mapear todos los stakeholders con:
- **Influence/Interest Matrix:** High/Medium/Low para cada dimensión
- **Communication Plans:** Frecuencia y método por stakeholder
- **Decision Authority:** Qué decisiones puede tomar cada stakeholder

```json
{
  "stakeholders": [
    {
      "name": "Stakeholder Name",
      "role": "Project-Sponsor|Product-Owner|End-User",
      "influence": "High|Medium|Low",
      "interest": "High|Medium|Low",
      "communicationPlan": {
        "frequency": "Weekly|Bi-weekly|Monthly",
        "method": "Email|Meeting|Dashboard",
        "content": "Progress updates, decisions needed"
      },
      "decisionAuthority": ["Budget approval", "Feature prioritization"]
    }
  ]
}
```

### 4. Team Structure - Organización Moderna
Definir estructura de equipo con metodologías ágiles:
- **Team Structure:** Scrum, Kanban, SAFe, Cross-Functional
- **Collaboration Tools:** Slack, Teams, Jira, Notion
- **Working Agreements:** Normas de trabajo del equipo
- **Capacity Planning:** Horas, velocity, utilización

```json
{
  "team": {
    "structure": "Scrum|Kanban|Cross-Functional",
    "methodology": "Agile|Lean|DevOps",
    "members": [
      {
        "name": "Team Member",
        "role": "Tech-Lead|Developer|QA-Engineer|UX-Designer",
        "responsibilities": ["Key responsibilities"],
        "availability": "80%|32h/week",
        "location": "Remote|Office|Hybrid"
      }
    ],
    "collaboration": {
      "tools": ["Slack", "Jira", "Figma"],
      "meetingCadence": {
        "standups": "Daily",
        "retrospectives": "Bi-weekly",
        "planning": "Weekly"
      }
    }
  }
}
```

### 5. Governance Framework - Toma de Decisiones
Implementar framework de governance moderno:
- **Decision Framework:** RACI, DACI, RAPID
- **Communication Plans:** Audiencia, frecuencia, contenido
- **Risk Management:** Registro de riesgos, mitigación, monitoreo

```json
{
  "governance": {
    "decisionMaking": {
      "framework": "RACI|DACI|RAPID",
      "authorities": [
        {
          "decision": "Technical architecture",
          "authority": "Tech Lead",
          "process": "Team consultation + approval"
        }
      ]
    },
    "riskManagement": {
      "approach": "Proactive",
      "riskRegister": [
        {
          "id": "RISK-001",
          "description": "Risk description",
          "category": "Technical|Business|Resource",
          "probability": "High|Medium|Low",
          "impact": "High|Medium|Low",
          "mitigation": "Mitigation strategy"
        }
      ]
    }
  }
}
```

## Proceso de Implementación Paso a Paso

### Fase 1: Preparación (30 min)
1. **Investigar Context:** Entender el proyecto y sus objetivos
2. **Identificar Stakeholders:** Mapear todos los involucrados
3. **Definir Scope:** Clarificar qué está incluido/excluido

### Fase 2: Project Charter (45 min)
1. **Vision & Mission:** Definir declaraciones claras
2. **SMART Objectives:** Crear objetivos específicos y medibles
3. **Success Criteria:** Establecer métricas de éxito
4. **Business Case:** Justificación y análisis costo-beneficio

### Fase 3: Team & Stakeholders (30 min)
1. **Team Structure:** Definir roles y responsabilidades
2. **Stakeholder Mapping:** Influence/Interest matrix
3. **Communication Plans:** Frecuencia y métodos por audiencia

### Fase 4: Governance (30 min)
1. **Decision Framework:** Elegir RACI/DACI/RAPID
2. **Risk Register:** Identificar y categorizar riesgos
3. **Quality Framework:** Definir estándares y procesos

## Checklist de Validación 2025

### ✅ Basic Info Completo
- [ ] Nombre del proyecto claro y único
- [ ] Descripción comprensiva (>20 caracteres)
- [ ] Versión semántica válida
- [ ] Status actual definido
- [ ] Tipo y categoría especificados
- [ ] Repository información completa

### ✅ Project Charter Robusto
- [ ] Vision statement inspiradora y clara
- [ ] Mission statement específica
- [ ] Objetivos SMART con owners y timelines
- [ ] Scope claramente definido (incluido/excluido)
- [ ] Success criteria medibles
- [ ] Business case documentado

### ✅ Stakeholder Management
- [ ] Todos los stakeholders identificados
- [ ] Influence/Interest matrix completada
- [ ] Communication plans específicos
- [ ] Decision authority claramente definida
- [ ] Contact information actualizada

### ✅ Team Structure Moderna
- [ ] Metodología ágil seleccionada
- [ ] Roles y responsabilidades claras
- [ ] Collaboration tools definidas
- [ ] Meeting cadence establecida
- [ ] Working agreements documentadas
- [ ] Capacity planning realizada

### ✅ Governance Framework
- [ ] Decision-making framework elegido
- [ ] Escalation paths definidos
- [ ] Risk register poblado
- [ ] Communication plan completo
- [ ] Quality assurance processes

## Mejores Prácticas 2025

### 🎯 Project Charter Excellence
- **Vision Statements:** Inspiradoras, específicas, orientadas al futuro
- **SMART Objectives:** Usar framework OKR para objetivos ambiciosos
- **Success Metrics:** Incluir leading y lagging indicators
- **Scope Management:** Usar técnicas como MoSCoW prioritization

### 👥 Modern Stakeholder Management
- **Stakeholder Personas:** Crear perfiles detallados como user personas
- **Influence Mapping:** Usar herramientas como stakeholder onion diagrams
- **Communication Automation:** Integrar con tools como Slack/Teams
- **Feedback Loops:** Establecer mecanismos regulares de feedback

### 🏗️ Agile Team Structures
- **Cross-functional Teams:** Minimizar dependencias externas
- **Psychological Safety:** Incluir working agreements sobre cultura
- **Remote-first Practices:** Optimizar para equipos distribuidos
- **Continuous Learning:** Incluir tiempo para upskilling

### 🎛️ Modern Governance
- **Decision Velocity:** Optimizar para decisiones rápidas y reversibles
- **Risk-based Thinking:** Integrar risk management en daily operations
- **Transparency:** Usar dashboards y metrics visibles para todos
- **Adaptive Planning:** Permitir cambios basados en learning

## Herramientas Recomendadas 2025

### Project Management
- **Jira/Linear:** Para tracking y planning
- **Notion/Confluence:** Para documentación
- **Miro/Figma:** Para visual collaboration
- **Slack/Teams:** Para comunicación

### Stakeholder Management
- **Stakeholder mapping tools:** Lucidchart, Miro
- **Communication automation:** Zapier, Microsoft Power Automate
- **Survey tools:** Typeform, Google Forms

### Risk Management
- **Risk registers:** Airtable, Notion databases
- **Monitoring:** Custom dashboards, DataDog
- **Incident management:** PagerDuty, Opsgenie

## Ejemplos de Implementación

### Startup Tech Project
```json
{
  "basicInfo": {
    "name": "AI-Powered Analytics Platform",
    "type": "Web-Application",
    "category": "B2B",
    "status": "Planning"
  },
  "team": {
    "structure": "Cross-Functional",
    "methodology": "Lean",
    "collaboration": {
      "tools": ["Slack", "Linear", "Figma"]
    }
  }
}
```

### Enterprise Integration
```json
{
  "governance": {
    "decisionMaking": {
      "framework": "RACI",
      "authorities": [
        {
          "decision": "Architecture decisions",
          "authority": "Enterprise Architect",
          "process": "Architecture Review Board"
        }
      ]
    }
  }
}
```

## Referencias y Recursos

### Frameworks de Project Management
- **PMI PMBOK 7th Edition:** Modern project management practices
- **SAFe 6.0:** Scaled Agile Framework
- **Scrum Guide 2020:** Latest Scrum practices
- **OKR Framework:** Objectives and Key Results

### Stakeholder Management
- **Stakeholder Theory:** Freeman's stakeholder management
- **Influence/Interest Grid:** Mendelow's matrix
- **Communication Planning:** PMBOK communication management

### Team Collaboration
- **Tuckman's Team Development:** Forming, Storming, Norming, Performing
- **Psychological Safety:** Google's Project Aristotle findings
- **Remote Team Best Practices:** GitLab's remote work guide

### Risk Management
- **ISO 31000:** Risk management principles
- **COSO ERM Framework:** Enterprise risk management
- **Agile Risk Management:** Risk-driven development

---

**Última actualización:** Diciembre 2025  
**Versión del schema:** 3.0.0  
**Compatibilidad:** JSON Schema Draft 2020-12
