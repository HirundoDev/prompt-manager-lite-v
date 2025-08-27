"""
Templates Testing
=================

Templates universales para estrategias de testing.
"""

def create_testing_strategy_template(theme, date_str, filename):
    """Marco de referencia para estrategias de testing"""
    return f'''# Estrategia de Testing - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Estrategia de Testing  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para estrategias de testing, adaptable a diferentes tecnologías y tipos de aplicación.

### Decisiones Clave a Capturar
- **Pirámide de testing** y niveles implementados
- **Frameworks y herramientas** elegidas
- **Estrategia de datos** para testing
- **CI/CD integration** y automatización
- **Coverage targets** y métricas

---

## 🏗️ Arquitectura de Testing

### Pirámide de Testing
**Decisión:** [Distribución de tipos de test]
```
        /\\
       /  \\
      / E2E \\     ← Few, expensive, slow
     /______\\
    /        \\
   /Integration\\   ← Some, moderate cost/speed
  /__________\\
 /            \\
/  Unit Tests  \\    ← Many, cheap, fast
/______________\\
```

#### Unit Tests (Base)
- **Porcentaje objetivo:** [70-80%]
- **Scope:** [Funciones individuales, clases, componentes]
- **Características:** [Fast, isolated, deterministic]

#### Integration Tests (Medio)
- **Porcentaje objetivo:** [15-25%]
- **Scope:** [APIs, database interactions, service integrations]
- **Características:** [Medium speed, realistic data]

#### End-to-End Tests (Top)
- **Porcentaje objetivo:** [5-15%]
- **Scope:** [Critical user journeys, full workflows]
- **Características:** [Slow, expensive, realistic environment]

---

## 🔧 Stack de Testing

### Testing Frameworks
**Decisión:** [Frameworks elegidos por tipo de test]

#### Unit Testing
- **Frontend:** [Jest, Vitest, Jasmine, Mocha]
- **Backend:** [Jest, PyTest, JUnit, Go Test, RSpec]
- **Mobile:** [XCTest, Espresso, Jest (React Native)]

#### Integration Testing
- **API Testing:** [Supertest, Postman, Insomnia, REST Assured]
- **Database Testing:** [Testcontainers, in-memory databases]
- **Service Testing:** [WireMock, Mockoon, MSW]

#### End-to-End Testing
- **Web:** [Cypress, Playwright, Selenium, Puppeteer]
- **Mobile:** [Appium, Detox, XCUITest, Espresso]
- **API:** [Postman Collections, Newman, Artillery]

### Utility Libraries
**Decisión:** [Herramientas de soporte]
- **Assertions:** [Chai, Should.js, custom matchers]
- **Test utilities:** [Testing Library, Enzyme, Test Utils]
- **Data generation:** [Faker.js, Factory Boy, random generators]

---

## 📊 Testing Strategy por Capa

### Frontend Testing
**Decisión:** [Estrategia específica para frontend]

#### Component Testing
```javascript
// Ejemplo Jest + Testing Library
import {{ render, screen, fireEvent }} from '@testing-library/react';
import Button from './Button';

describe('Button component', () => {{
  test('renders with correct text', () => {{
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  }});

  test('calls onClick when clicked', () => {{
    const handleClick = jest.fn();
    render(<Button onClick={{handleClick}}>Click me</Button>);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  }});
}});
```

#### Integration Testing
- **State management:** [Redux, Context, Pinia testing]
- **Routing:** [React Router, Vue Router testing]
- **API integration:** [Mock Service Worker, axios mocking]

### Backend Testing
**Decisión:** [Estrategia específica para backend]

#### Unit Testing
```python
# Ejemplo PyTest
import pytest
from app.services import UserService

class TestUserService:
    def test_create_user_success(self):
        service = UserService()
        user_data = {{"name": "John", "email": "john@example.com"}}
        
        user = service.create_user(user_data)
        
        assert user.name == "John"
        assert user.email == "john@example.com"
        assert user.id is not None

    def test_create_user_invalid_email(self):
        service = UserService()
        user_data = {{"name": "John", "email": "invalid-email"}}
        
        with pytest.raises(ValidationError):
            service.create_user(user_data)
```

#### API Testing
```javascript
// Ejemplo Supertest
const request = require('supertest');
const app = require('../app');

describe('POST /api/users', () => {{
  test('creates a new user', async () => {{
    const userData = {{
      name: 'John Doe',
      email: 'john@example.com'
    }};

    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);

    expect(response.body).toMatchObject({{
      id: expect.any(Number),
      name: 'John Doe',
      email: 'john@example.com'
    }});
  }});
}});
```

---

## 🗃️ Test Data Management

### Data Strategy
**Decisión:** [Estrategia de datos de prueba]
- **Fixtures:** [Static test data files]
- **Factories:** [Dynamic data generation]
- **Seeders:** [Database initialization]
- **Anonymization:** [Production data sanitization]

### Database Testing
**Decisión:** [Estrategia de base de datos para testing]
- **In-memory database:** [SQLite, H2, MongoMemoryServer]
- **Testcontainers:** [Docker containers for testing]
- **Test database:** [Dedicated testing instance]
- **Transactions rollback:** [Isolated test execution]

### Test Isolation
**Decisión:** [Estrategia de aislamiento]
```javascript
// Setup y teardown por test
beforeEach(async () => {{
  // Setup fresh state
  await database.migrate();
  await database.seed();
}});

afterEach(async () => {{
  // Cleanup after each test
  await database.cleanup();
}});
```

---

## 🤖 Test Automation

### CI/CD Integration
**Decisión:** [Integración con pipeline de CI/CD]

#### Pipeline Configuration
```yaml
# GitHub Actions ejemplo
name: Test Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run unit tests
        run: npm run test:unit
        
      - name: Run integration tests
        run: npm run test:integration
        
      - name: Run E2E tests
        run: npm run test:e2e
        
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### Parallel Execution
**Decisión:** [Estrategia de paralelización]
- **Test splitting:** [Por archivo, por tiempo, por tipo]
- **Matrix testing:** [Multiple OS, Node versions, browsers]
- **Distributed testing:** [Multiple machines, cloud services]

---

## 📈 Coverage y Métricas

### Coverage Targets
**Decisión:** [Objetivos de cobertura]
- **Unit tests:** [80-90% line coverage]
- **Integration tests:** [60-70% integration paths]
- **E2E tests:** [100% critical user journeys]

### Coverage Tools
**Decisión:** [Herramientas de medición]
- **JavaScript:** [Istanbul/NYC, Jest coverage]
- **Python:** [Coverage.py, pytest-cov]
- **Java:** [JaCoCo, Cobertura]
- **Go:** [Built-in go test -cover]

### Quality Gates
**Decisión:** [Criterios de calidad]
```javascript
// jest.config.js
module.exports = {{
  coverageThreshold: {{
    global: {{
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }}
  }},
  collectCoverageFrom: [
    'src/**/*.{{js,ts}}',
    '!src/**/*.test.{{js,ts}}',
    '!src/**/*.spec.{{js,ts}}'
  ]
}};
```

---

## 🔍 Test Types Específicos

### Security Testing
**Decisión:** [Testing de seguridad implementado]
- **SAST:** [Static Application Security Testing]
- **DAST:** [Dynamic Application Security Testing]
- **Dependency scanning:** [Known vulnerabilities]
- **Authentication/Authorization:** [Access control testing]

### Performance Testing
**Decisión:** [Testing de performance]
- **Load testing:** [Normal expected load]
- **Stress testing:** [Beyond normal capacity]
- **Spike testing:** [Sudden load increases]
- **Volume testing:** [Large amounts of data]

#### Tools
- **Web:** [Artillery, JMeter, k6, Lighthouse CI]
- **API:** [Apache Bench, wrk, Artillery]
- **Database:** [pgbench, sysbench]

### Accessibility Testing
**Decisión:** [Testing de accesibilidad]
- **Automated:** [axe-core, pa11y, Lighthouse]
- **Manual:** [Screen reader testing, keyboard navigation]
- **Standards:** [WCAG 2.1 AA compliance]

---

## 🎭 Mocking y Stubs

### Mocking Strategy
**Decisión:** [Estrategia de mocking]
- **External APIs:** [MSW, WireMock, Nock]
- **Database:** [In-memory, test doubles]
- **Time/Dates:** [Sinon fake timers, Jest timers]
- **File system:** [Mock-fs, memfs]

### Service Virtualization
**Decisión:** [Virtualización de servicios]
- **Third-party APIs:** [Stubbed responses]
- **Microservices:** [Contract testing, Pact]
- **Legacy systems:** [Service virtualization tools]

---

## 🚦 Test Environment Management

### Environment Strategy
**Decisión:** [Gestión de ambientes de testing]
- **Local development:** [Docker Compose, local services]
- **CI environment:** [Ephemeral, containerized]
- **Integration environment:** [Shared, stable services]
- **Staging environment:** [Production-like setup]

### Configuration Management
```javascript
// config/test.js
module.exports = {{
  database: {{
    host: process.env.TEST_DB_HOST || 'localhost',
    port: process.env.TEST_DB_PORT || 5433,
    database: 'test_database'
  }},
  api: {{
    baseUrl: 'http://localhost:3001',
    timeout: 5000
  }},
  features: {{
    enableNewFeature: true // Feature flags for testing
  }}
}};
```

---

## 🔄 Continuous Testing

### Testing in Development
**Decisión:** [Testing durante desarrollo]
- **Test-Driven Development (TDD):** [Red-Green-Refactor]
- **Behavior-Driven Development (BDD):** [Gherkin scenarios]
- **Watch mode:** [Automatic test re-runs]

### Testing in CI/CD
**Decisión:** [Testing en pipeline]
- **Pre-commit hooks:** [Basic linting, unit tests]
- **Pull request checks:** [Full test suite]
- **Deployment gates:** [Integration and E2E tests]
- **Post-deployment:** [Smoke tests, monitoring]

### Flaky Test Management
**Decisión:** [Manejo de tests inconsistentes]
- **Detection:** [Retry mechanisms, test analytics]
- **Quarantine:** [Separate flaky tests from stable suite]
- **Root cause analysis:** [Logging, debugging tools]
- **Prevention:** [Better test design, deterministic tests]

---

## 📋 Testing Checklist

### Pre-Development
- [ ] **Testing strategy defined:** [Types, tools, coverage targets]
- [ ] **Test environment setup:** [Local, CI, staging]
- [ ] **Data strategy established:** [Fixtures, factories, cleanup]

### During Development
- [ ] **Unit tests written:** [For each function/component]
- [ ] **Integration tests added:** [For API endpoints, services]
- [ ] **Mocks configured:** [External dependencies isolated]

### Pre-Deployment
- [ ] **E2E tests passing:** [Critical user journeys verified]
- [ ] **Performance tests executed:** [Load/stress testing]
- [ ] **Security scans completed:** [Vulnerability assessment]

### Post-Deployment
- [ ] **Smoke tests executed:** [Basic functionality verified]
- [ ] **Monitoring enabled:** [Error tracking, performance metrics]
- [ ] **Test results documented:** [Coverage reports, test reports]

---

## 🔄 Próximos Pasos

### Setup Inicial
- [ ] [Configurar frameworks de testing]
- [ ] [Setup test environment]
- [ ] [Definir data strategy]

### Implementation
- [ ] [Escribir unit tests base]
- [ ] [Configurar integration testing]
- [ ] [Setup E2E testing framework]

### Automation
- [ ] [Integrar tests en CI/CD]
- [ ] [Configurar coverage reporting]
- [ ] [Setup automated test runs]

### Optimization
- [ ] [Optimizar test performance]
- [ ] [Implementar parallel execution]
- [ ] [Setup test analytics]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
