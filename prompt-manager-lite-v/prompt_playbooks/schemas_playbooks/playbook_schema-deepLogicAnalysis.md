# Schema Playbook — deepLogicAnalysis

**Propósito:** Crear análisis comprehensivos de código siguiendo mejores prácticas de static analysis 2025, con complexity metrics, security vulnerability detection, maintainability assessment y automated quality gates con AI-enhanced analysis capabilities.

**Ubicación:** `schemas/master_blueprint_parts/deepLogicAnalysis.json`

---

## **METODOLOGÍA 2025: STATIC ANALYSIS & CODE QUALITY**

### **1. INVESTIGACIÓN PREVIA REQUERIDA**
Antes de crear el análisis, investigar:
- **Static Analysis Tools:** SonarQube, ESLint, CodeQL, Semgrep, Checkmarx
- **Complexity Metrics:** Cyclomatic, cognitive, Halstead, maintainability index
- **Security Standards:** OWASP Top 10, NIST guidelines, CERT coding standards
- **Quality Frameworks:** ISO 25010, SOLID principles, Clean Code practices
- **AI-Enhanced Analysis:** Machine learning for pattern detection, automated code review

### **2. ESTRUCTURA MODERNA DEL SCHEMA**

#### **A. METADATA SECTION (Requerido)**
```json
{
  "metadata": {
    "name": "Payment Service Logic Analysis",
    "version": "1.2.0",
    "timestamp": "2025-01-15T14:30:00Z",
    "description": "Comprehensive analysis of payment processing logic",
    "analyst": {
      "name": "Jane Smith",
      "role": "Senior Software Architect",
      "email": "jane.smith@company.com"
    },
    "tools": [
      {
        "name": "SonarQube",
        "version": "9.9",
        "type": "static-analyzer"
      }
    ],
    "standards": ["OWASP", "SOLID", "Clean-Code"]
  }
}
```

#### **B. ANALYSIS SCOPE SECTION (Requerido)**
```json
{
  "analysisScope": {
    "components": [
      {
        "name": "PaymentProcessor",
        "type": "service|module|class|function|package",
        "path": "src/services/payment/PaymentProcessor.ts",
        "language": "typescript|javascript|python|java|csharp",
        "framework": "Node.js",
        "linesOfCode": 450,
        "criticality": "low|medium|high|critical",
        "dependencies": ["stripe", "paypal-sdk", "database"]
      }
    ],
    "exclusions": [
      {
        "path": "node_modules/**",
        "reason": "Third-party dependencies",
        "pattern": "*.test.js"
      }
    ],
    "boundaries": {
      "maxComplexity": 15,
      "includeTests": true,
      "includeThirdParty": false
    }
  }
}
```

#### **C. QUALITY METRICS SECTION (Core)**
```json
{
  "qualityMetrics": {
    "complexity": {
      "cyclomatic": {
        "average": 8.5,
        "maximum": 23,
        "distribution": {
          "low": 15,      // Functions with complexity 1-10
          "moderate": 8,  // Functions with complexity 11-20
          "high": 3,      // Functions with complexity 21-50
          "veryHigh": 1   // Functions with complexity >50
        }
      },
      "cognitive": {
        "average": 12.3,
        "maximum": 28,
        "threshold": 15  // SonarQube standard
      },
      "halstead": {
        "volume": 1250.5,
        "difficulty": 18.2,
        "effort": 22759.1,
        "timeToUnderstand": 1264.4
      },
      "maintainabilityIndex": 72  // Microsoft maintainability index (0-100)
    },
    "codeQuality": {
      "duplication": {
        "percentage": 3.2,
        "blocks": 5,
        "lines": 45
      },
      "coverage": {
        "line": 85.5,
        "branch": 78.2,
        "function": 92.1,
        "statement": 88.7
      },
      "technicalDebt": {
        "ratio": 0.8,      // Debt ratio percentage
        "minutes": 120,    // Time to fix debt
        "rating": "A|B|C|D|E"
      },
      "codeSmells": {
        "total": 15,
        "blocker": 0,
        "critical": 2,
        "major": 8,
        "minor": 5,
        "info": 0
      }
    },
    "security": {
      "vulnerabilities": {
        "total": 2,
        "critical": 0,
        "high": 1,
        "medium": 1,
        "low": 0
      },
      "hotspots": {
        "total": 5,
        "toReview": 3,
        "reviewed": 2
      },
      "securityRating": "A|B|C|D|E"
    },
    "performance": {
      "algorithmicComplexity": {
        "timeComplexity": "O(n log n)",
        "spaceComplexity": "O(n)",
        "worstCase": "O(n²)"
      },
      "memoryUsage": {
        "estimated": "~50MB",
        "leakRisk": "low|medium|high"
      },
      "concurrency": {
        "threadSafety": true,
        "raceConditions": 0,
        "deadlockRisk": "low|medium|high"
      }
    }
  }
}
```

#### **D. FINDINGS SECTION (Core)**
```json
{
  "findings": [
    {
      "id": "COMPLEX-001",
      "type": "complexity-violation|code-smell|bug|vulnerability|performance-issue",
      "severity": "blocker|critical|major|minor|info",
      "component": {
        "name": "PaymentProcessor",
        "path": "src/services/payment/PaymentProcessor.ts",
        "line": 145,
        "column": 12,
        "function": "processPayment",
        "class": "PaymentProcessor"
      },
      "description": "Function has cyclomatic complexity of 23, exceeding threshold of 15",
      "message": "Reduce function complexity",
      "rule": {
        "id": "complexity",
        "name": "Cyclomatic Complexity",
        "category": "maintainability",
        "standard": "SonarQube"
      },
      "impact": {
        "reliability": "medium",
        "security": "low",
        "maintainability": "high",
        "performance": "low"
      },
      "effort": {
        "minutes": 180,
        "complexity": "trivial|easy|medium|hard|complex",
        "skillLevel": "junior|mid|senior|expert"
      },
      "recommendation": {
        "action": "Extract smaller functions and use strategy pattern",
        "priority": "low|medium|high|urgent",
        "alternatives": [
          "Split into multiple functions",
          "Use command pattern",
          "Implement state machine"
        ],
        "examples": [
          {
            "before": "if (type === 'credit') { /* 50 lines */ }",
            "after": "return this.processCreditCard(data);",
            "explanation": "Extract payment type logic into separate methods"
          }
        ],
        "references": [
          "https://refactoring.guru/extract-method",
          "Clean Code by Robert Martin, Chapter 3"
        ]
      },
      "context": {
        "codeSnippet": "function processPayment(data) { if (data.type === 'credit') { ... } }",
        "surroundingCode": "class PaymentProcessor { ... }",
        "callStack": ["PaymentService.process", "PaymentProcessor.processPayment"],
        "dataFlow": ["input validation", "payment processing", "result handling"]
      },
      "metadata": {
        "tool": "SonarQube",
        "ruleVersion": "9.9",
        "confidence": 0.95,
        "falsePositiveRisk": "low|medium|high",
        "tags": ["complexity", "maintainability", "refactoring"]
      }
    }
  ]
}
```

#### **E. DOMAINS SECTION (Business Logic)**
```json
{
  "domains": [
    {
      "name": "Payment Processing",
      "description": "Core payment processing logic and workflows",
      "businessRules": [
        {
          "id": "BR-001",
          "name": "Payment Validation",
          "description": "All payments must be validated before processing",
          "implementation": "validatePayment() function",
          "validation": "Unit tests and integration tests",
          "exceptions": ["Emergency bypass for system admin"]
        }
      ],
      "invariants": [
        {
          "condition": "amount > 0",
          "description": "Payment amount must be positive",
          "enforcement": "Input validation at API layer",
          "violations": 0
        }
      ],
      "edgeCases": [
        {
          "scenario": "Network timeout during payment",
          "description": "Payment gateway becomes unavailable",
          "handling": "Retry with exponential backoff, max 3 attempts",
          "testCoverage": true,
          "riskLevel": "high"
        }
      ],
      "failureModes": [
        {
          "mode": "Gateway timeout",
          "cause": "Network latency or gateway overload",
          "effect": "Payment processing failure",
          "detection": "Timeout monitoring and alerts",
          "mitigation": "Circuit breaker pattern with fallback",
          "probability": "low"
        }
      ],
      "decisionPoints": [
        {
          "id": "DP-001",
          "context": "Payment retry strategy",
          "alternatives": [
            {
              "option": "Immediate retry",
              "pros": ["Fast recovery", "Simple implementation"],
              "cons": ["May overwhelm failing service", "No backoff"],
              "complexity": 3,
              "risk": "medium"
            },
            {
              "option": "Exponential backoff",
              "pros": ["Reduces load on failing service", "Better success rate"],
              "cons": ["Longer recovery time", "More complex"],
              "complexity": 7,
              "risk": "low"
            }
          ],
          "chosen": "Exponential backoff",
          "rationale": "Better long-term reliability despite complexity",
          "tradeoffs": "Increased latency for improved reliability",
          "reviewDate": "2025-06-01",
          "links": {
            "adr": "docs/adr/ADR-015-payment-retry.md",
            "code": ["src/services/payment/RetryHandler.ts"],
            "documentation": "docs/payment-processing.md"
          }
        }
      ]
    }
  ]
}
```

#### **F. CRITICAL PATHS SECTION**
```json
{
  "criticalPaths": [
    {
      "id": "CP-001",
      "name": "Credit Card Payment Flow",
      "description": "End-to-end credit card payment processing",
      "criticality": "critical",
      "steps": [
        {
          "order": 1,
          "action": "Validate payment data",
          "component": "PaymentValidator",
          "duration": "50ms",
          "complexity": 5,
          "errorHandling": "Return validation errors"
        },
        {
          "order": 2,
          "action": "Process payment with gateway",
          "component": "PaymentGateway",
          "duration": "2000ms",
          "complexity": 12,
          "errorHandling": "Retry with backoff"
        }
      ],
      "preconditions": [
        {
          "condition": "User authenticated",
          "validation": "JWT token validation",
          "fallback": "Redirect to login"
        }
      ],
      "postconditions": [
        {
          "condition": "Payment recorded in database",
          "verification": "Database transaction confirmation",
          "cleanup": "Release payment locks"
        }
      ],
      "metrics": {
        "executionTime": "2.5s average",
        "throughput": "100 payments/minute",
        "errorRate": 0.02,
        "successRate": 0.98
      },
      "monitoring": {
        "alerts": ["payment_failure_rate > 5%", "avg_response_time > 5s"],
        "dashboards": ["Payment Processing Dashboard"],
        "logs": ["payment.log", "gateway.log"]
      }
    }
  ]
}
```

#### **G. RISKS SECTION**
```json
{
  "risks": [
    {
      "id": "RISK-001",
      "category": "security|performance|maintainability|business|operational",
      "description": "Potential SQL injection in payment logging",
      "likelihood": "very-low|low|medium|high|very-high",
      "impact": "very-low|low|medium|high|very-high",
      "riskScore": 15,  // likelihood × impact (1-25 scale)
      "triggers": [
        "Unsanitized user input in log statements",
        "Dynamic SQL query construction"
      ],
      "indicators": [
        "Unusual database query patterns",
        "Unexpected log entries",
        "Security scanner alerts"
      ],
      "mitigations": [
        {
          "strategy": "Use parameterized queries",
          "action": "Replace string concatenation with prepared statements",
          "owner": "Security Team",
          "timeline": "1 week",
          "cost": "Low",
          "effectiveness": "high"
        }
      ],
      "contingency": {
        "plan": "Immediate database isolation and forensic analysis",
        "resources": "Security incident response team",
        "timeline": "4 hours maximum response time"
      }
    }
  ]
}
```

#### **H. CONTROLS SECTION**
```json
{
  "controls": [
    {
      "id": "CTRL-001",
      "name": "Complexity Monitoring",
      "type": "monitor|alert|test|gate|review|audit",
      "target": "Cyclomatic complexity",
      "description": "Monitor code complexity trends",
      "frequency": "on-change|continuous|daily|weekly|monthly",
      "automation": {
        "automated": true,
        "tool": "SonarQube",
        "configuration": {
          "threshold": 15,
          "failBuild": true
        }
      },
      "thresholds": {
        "warning": "complexity > 10",
        "critical": "complexity > 15",
        "acceptable": "complexity <= 10"
      },
      "actions": [
        {
          "trigger": "complexity > 15",
          "action": "Block pull request merge",
          "owner": "Development Team",
          "escalation": "Tech Lead review required"
        }
      ]
    }
  ]
}
```

#### **I. RECOMMENDATIONS SECTION**
```json
{
  "recommendations": {
    "immediate": [
      {
        "action": "Fix critical security vulnerabilities",
        "rationale": "Prevent potential security breaches",
        "effort": "4 hours",
        "impact": "High security improvement",
        "priority": 1
      }
    ],
    "shortTerm": [
      {
        "action": "Reduce complexity in PaymentProcessor.processPayment",
        "rationale": "Improve maintainability and reduce bug risk",
        "effort": "1 day",
        "impact": "Better code maintainability",
        "timeline": "Next sprint"
      }
    ],
    "longTerm": [
      {
        "action": "Implement comprehensive monitoring dashboard",
        "rationale": "Proactive issue detection and resolution",
        "effort": "2 weeks",
        "impact": "Improved operational visibility",
        "timeline": "Next quarter"
      }
    ],
    "architectural": [
      {
        "pattern": "Circuit Breaker",
        "description": "Implement circuit breaker for external service calls",
        "benefits": ["Improved resilience", "Faster failure detection"],
        "tradeoffs": ["Additional complexity", "Configuration overhead"]
      }
    ]
  }
}
```

---

## **3. PROCESO DE IMPLEMENTACIÓN**

### **PASO 1: TOOL SETUP & CONFIGURATION**
1. **Static Analysis Tools:** Configure SonarQube, ESLint, security scanners
2. **Quality Gates:** Set up automated quality thresholds
3. **CI/CD Integration:** Integrate analysis into build pipeline
4. **Baseline Establishment:** Create initial quality baseline

### **PASO 2: SCOPE DEFINITION**
1. **Component Identification:** Map all components for analysis
2. **Boundary Setting:** Define analysis scope and exclusions
3. **Criticality Assessment:** Classify components by business impact
4. **Dependency Mapping:** Document component dependencies

### **PASO 3: METRICS COLLECTION**
1. **Complexity Analysis:** Calculate cyclomatic, cognitive, Halstead metrics
2. **Quality Assessment:** Measure duplication, coverage, technical debt
3. **Security Scanning:** Identify vulnerabilities and security hotspots
4. **Performance Analysis:** Assess algorithmic complexity and resource usage

### **PASO 4: FINDINGS ANALYSIS**
1. **Issue Classification:** Categorize findings by type and severity
2. **Impact Assessment:** Evaluate business and technical impact
3. **Effort Estimation:** Calculate remediation effort and complexity
4. **Prioritization:** Rank findings by risk and business value

### **PASO 5: DOMAIN MODELING**
1. **Business Logic Mapping:** Document business rules and invariants
2. **Edge Case Identification:** Catalog edge cases and failure modes
3. **Decision Documentation:** Record architectural decisions and rationale
4. **Risk Assessment:** Identify and evaluate business and technical risks

### **PASO 6: MONITORING & CONTROLS**
1. **Control Implementation:** Set up automated quality controls
2. **Monitoring Setup:** Configure continuous monitoring and alerting
3. **Dashboard Creation:** Build visualization for key metrics
4. **Process Integration:** Embed controls into development workflow

---

## **4. CHECKLIST DE COMPLETITUD**

### **📋 ANALYSIS SETUP**
- [ ] Static analysis tools configured and integrated
- [ ] Quality gates defined with appropriate thresholds
- [ ] Analysis scope clearly defined with exclusions
- [ ] Baseline metrics established for comparison

### **📋 METRICS & FINDINGS**
- [ ] Complexity metrics calculated for all components
- [ ] Code quality issues identified and categorized
- [ ] Security vulnerabilities assessed and prioritized
- [ ] Performance bottlenecks identified and documented

### **📋 BUSINESS CONTEXT**
- [ ] Business domains mapped with rules and invariants
- [ ] Critical paths documented with preconditions/postconditions
- [ ] Edge cases and failure modes cataloged
- [ ] Architectural decisions recorded with rationale

### **📋 RISK & CONTROLS**
- [ ] Risks identified with likelihood and impact assessment
- [ ] Mitigation strategies defined with owners and timelines
- [ ] Quality controls implemented with automation
- [ ] Monitoring and alerting configured

### **📋 RECOMMENDATIONS**
- [ ] Immediate actions identified and prioritized
- [ ] Short-term improvements planned with timelines
- [ ] Long-term architectural recommendations documented
- [ ] Implementation roadmap created with milestones

---

## **5. MEJORES PRÁCTICAS 2025**

### **🎯 ANALYSIS AUTOMATION**
- **Continuous Integration:** Run analysis on every commit
- **Quality Gates:** Block deployments that don't meet quality standards
- **Automated Remediation:** Use AI to suggest and apply fixes
- **Trend Analysis:** Track quality metrics over time

### **🎯 COMPLEXITY MANAGEMENT**
- **Cyclomatic Complexity:** Keep functions under 15 complexity
- **Cognitive Complexity:** Limit cognitive load to 15 (SonarQube standard)
- **Function Length:** Maintain functions under 50 lines
- **Class Size:** Keep classes focused with single responsibility

### **🎯 SECURITY INTEGRATION**
- **Shift-Left Security:** Integrate security scanning early in development
- **OWASP Compliance:** Follow OWASP Top 10 guidelines
- **Dependency Scanning:** Monitor third-party dependencies for vulnerabilities
- **Secret Detection:** Prevent secrets from being committed to code

### **🎯 PERFORMANCE OPTIMIZATION**
- **Algorithmic Analysis:** Optimize time and space complexity
- **Memory Management:** Prevent memory leaks and optimize usage
- **Concurrency Safety:** Ensure thread-safe code design
- **Resource Monitoring:** Track resource usage patterns

---

## **6. HERRAMIENTAS RECOMENDADAS 2025**

### **📊 STATIC ANALYSIS**
- **SonarQube:** Comprehensive code quality and security analysis
- **CodeQL:** Semantic code analysis for security vulnerabilities
- **ESLint:** JavaScript/TypeScript linting with custom rules
- **Semgrep:** Fast, customizable static analysis
- **Checkmarx:** Enterprise security scanning

### **📊 COMPLEXITY ANALYSIS**
- **SonarQube:** Built-in complexity metrics
- **Code Climate:** Maintainability and technical debt analysis
- **NDepend:** .NET code analysis and metrics
- **Understand:** Code comprehension and metrics tool
- **Lizard:** Cyclomatic complexity analyzer

### **📊 SECURITY SCANNING**
- **Snyk:** Vulnerability scanning for dependencies
- **OWASP Dependency Check:** Open source vulnerability scanner
- **Bandit:** Python security linter
- **Brakeman:** Ruby on Rails security scanner
- **SpotBugs:** Java static analysis for bugs

### **📊 AI-ENHANCED ANALYSIS**
- **DeepCode:** AI-powered code review
- **Amazon CodeGuru:** ML-powered code analysis
- **GitHub Copilot:** AI pair programming
- **Tabnine:** AI code completion and analysis
- **Codacy:** Automated code review with AI insights

---

## **7. EJEMPLO COMPLETO**

```json
{
  "metadata": {
    "name": "Payment Service Logic Analysis",
    "version": "1.2.0",
    "timestamp": "2025-01-15T14:30:00Z",
    "analyst": {
      "name": "Jane Smith",
      "role": "Senior Software Architect"
    },
    "tools": [
      {"name": "SonarQube", "version": "9.9", "type": "static-analyzer"}
    ],
    "standards": ["OWASP", "SOLID", "Clean-Code"]
  },
  "analysisScope": {
    "components": [
      {
        "name": "PaymentProcessor",
        "type": "service",
        "path": "src/services/payment/PaymentProcessor.ts",
        "language": "typescript",
        "criticality": "critical"
      }
    ]
  },
  "qualityMetrics": {
    "complexity": {
      "cyclomatic": {"average": 8.5, "maximum": 23},
      "maintainabilityIndex": 72
    },
    "security": {
      "vulnerabilities": {"total": 2, "high": 1},
      "securityRating": "B"
    }
  },
  "findings": [
    {
      "id": "COMPLEX-001",
      "type": "complexity-violation",
      "severity": "major",
      "component": {
        "name": "PaymentProcessor",
        "path": "src/services/payment/PaymentProcessor.ts",
        "line": 145,
        "function": "processPayment"
      },
      "description": "Function has cyclomatic complexity of 23, exceeding threshold of 15",
      "recommendation": {
        "action": "Extract smaller functions and use strategy pattern",
        "priority": "high"
      }
    }
  ],
  "domains": [
    {
      "name": "Payment Processing",
      "businessRules": [
        {
          "id": "BR-001",
          "name": "Payment Validation",
          "description": "All payments must be validated before processing"
        }
      ],
      "edgeCases": [
        {
          "scenario": "Network timeout during payment",
          "handling": "Retry with exponential backoff",
          "riskLevel": "high"
        }
      ]
    }
  ],
  "risks": [
    {
      "id": "RISK-001",
      "category": "security",
      "description": "Potential SQL injection in payment logging",
      "likelihood": "low",
      "impact": "high",
      "riskScore": 15
    }
  ],
  "controls": [
    {
      "id": "CTRL-001",
      "name": "Complexity Monitoring",
      "type": "monitor",
      "target": "Cyclomatic complexity",
      "frequency": "on-change",
      "automation": {"automated": true, "tool": "SonarQube"}
    }
  ]
}
```

---

## **8. REFERENCIAS Y RECURSOS**

### **📚 STANDARDS & FRAMEWORKS**
- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **NIST Cybersecurity Framework:** https://www.nist.gov/cyberframework
- **ISO/IEC 25010:** Software quality model
- **SOLID Principles:** Object-oriented design principles
- **Clean Code:** Robert C. Martin's coding principles

### **📚 TOOLS & PLATFORMS**
- **SonarQube Documentation:** https://docs.sonarqube.org/
- **ESLint Rules:** https://eslint.org/docs/rules/
- **CodeQL Documentation:** https://codeql.github.com/docs/
- **OWASP Dependency Check:** https://owasp.org/www-project-dependency-check/
- **Semgrep Rules:** https://semgrep.dev/explore

### **📚 BEST PRACTICES**
- **Static Analysis Best Practices:** Industry guidelines for effective analysis
- **Code Review Guidelines:** Peer review best practices
- **Security by Design:** Secure coding principles
- **Performance Optimization:** Code performance best practices
- **Technical Debt Management:** Strategies for managing technical debt

---

**Última actualización:** 2025-01-15  
**Versión del playbook:** 2.0  
**Compatibilidad:** JSON Schema Draft-07, mejores prácticas 2025
