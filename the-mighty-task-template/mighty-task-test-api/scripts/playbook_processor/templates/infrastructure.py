"""
Templates Infrastructure
========================

Templates universales para deployment, DevOps e infraestructura.
"""

def create_deployment_template(theme, date_str, filename):
    """Marco de referencia para deployment e infraestructura"""
    return f'''# Deployment e Infraestructura - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Deployment e Infraestructura  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para estrategias de deployment e infraestructura, adaptable a diferentes proveedores y tecnologías.

### Decisiones Clave a Capturar
- **Estrategia de deployment** elegida
- **Cloud provider** y servicios
- **Containerización** y orquestación
- **CI/CD pipeline** implementado
- **Monitoreo** y observabilidad

---

## ☁️ Cloud Strategy

### Cloud Provider
**Decisión:** [Proveedor de cloud elegido]
- **AWS** / **Google Cloud** / **Azure** / **Digital Ocean** / **Vercel** / **Netlify**
- **Multi-cloud** / **Hybrid** / **On-premise**
- **Justificación:** [Razones para la elección]

### Región y Disponibilidad
**Decisión:** [Configuración geográfica]
- **Primary region:** [us-east-1, eu-west-1, etc.]
- **Secondary regions:** [Para disaster recovery]
- **Availability zones:** [Multi-AZ deployment]
- **Edge locations:** [CDN, caching]

### Cost Optimization
**Decisión:** [Estrategia de optimización de costos]
- **Reserved instances:** [Long-term commitments]
- **Spot instances:** [Para workloads no críticos]
- **Auto-scaling:** [Scale-to-zero capabilities]
- **Resource tagging:** [Cost allocation]

---

## 🐳 Containerización

### Container Strategy
**Decisión:** [Estrategia de contenedores]
- **Docker:** [Sí/No y configuración]
- **Podman** / **Containerd** / **Other**
- **Multi-stage builds:** [Optimización de imágenes]

### Container Registry
**Decisión:** [Registro de imágenes]
- **Docker Hub** / **AWS ECR** / **Google Container Registry** / **Azure Container Registry**
- **Private vs Public:** [Visibilidad de imágenes]
- **Image scanning:** [Security vulnerabilities]

### Dockerfile Strategy
```dockerfile
# Ejemplo de Dockerfile optimizado
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

---

## 🚀 Deployment Strategy

### Deployment Pattern
**Decisión:** [Patrón de deployment elegido]
- **Rolling deployment** / **Blue-Green** / **Canary** / **A/B Testing**
- **Recreate** / **Shadow** / **Feature flags**

### Infrastructure as Code
**Decisión:** [Herramienta de IaC]
- **Terraform** / **AWS CloudFormation** / **Azure ARM** / **Pulumi**
- **Ansible** / **Chef** / **Puppet** (para configuración)

### Environment Strategy
**Decisión:** [Estrategia de ambientes]
```
Development → Staging → Production
           ↘ Testing ↗
```

- **Development:** [Local development environment]
- **Staging:** [Pre-production testing]
- **Production:** [Live environment]
- **Testing:** [Automated testing environment]

---

## ⚙️ CI/CD Pipeline

### CI/CD Platform
**Decisión:** [Plataforma de CI/CD]
- **GitHub Actions** / **GitLab CI** / **Jenkins** / **Azure DevOps**
- **CircleCI** / **Travis CI** / **AWS CodePipeline**

### Pipeline Stages
**Decisión:** [Etapas del pipeline]
1. **Source:** [Code checkout]
2. **Build:** [Compile, bundle, test]
3. **Test:** [Unit, integration, security]
4. **Package:** [Docker build, artifacts]
5. **Deploy:** [Environment deployment]
6. **Verify:** [Health checks, smoke tests]

### Pipeline Configuration
```yaml
# Ejemplo GitHub Actions
name: Deploy Pipeline
on:
  push:
    branches: [main]
    
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
      - name: Build application
        run: npm run build
      - name: Build Docker image
        run: docker build -t app:${{{{ github.sha }}}} .
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        run: ./deploy-staging.sh
```

---

## 🎛️ Orchestration

### Container Orchestration
**Decisión:** [Sistema de orquestación]
- **Kubernetes** / **Docker Swarm** / **AWS ECS** / **Google Cloud Run**
- **Nomad** / **None (simple containers)**

### Kubernetes Configuration
**Decisión:** [Si se usa Kubernetes]
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: [app-name]
spec:
  replicas: 3
  selector:
    matchLabels:
      app: [app-name]
  template:
    metadata:
      labels:
        app: [app-name]
    spec:
      containers:
      - name: [app-name]
        image: [image-name]:[tag]
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
```

### Service Discovery
**Decisión:** [Estrategia de service discovery]
- **Kubernetes Services** / **AWS Service Discovery** / **Consul**
- **DNS-based** / **Load balancer-based**

---

## 🌐 Networking y Security

### Load Balancing
**Decisión:** [Estrategia de load balancing]
- **Application Load Balancer** / **Network Load Balancer**
- **NGINX** / **HAProxy** / **Traefik**
- **Health checks:** [Endpoint monitoring]

### SSL/TLS Configuration
**Decisión:** [Configuración de certificados]
- **Let's Encrypt** / **AWS Certificate Manager** / **Custom certificates**
- **Automatic renewal:** [Cert-manager, etc.]
- **TLS termination:** [Load balancer vs application]

### Security Groups/Firewall
**Decisión:** [Configuración de red]
- **Inbound rules:** [Port 80, 443, SSH, etc.]
- **Outbound rules:** [Database, external APIs]
- **Network segmentation:** [VPC, subnets]

---

## 💾 Data y Storage

### Database Deployment
**Decisión:** [Estrategia de base de datos]
- **Managed service:** [RDS, Cloud SQL, etc.]
- **Self-hosted:** [On containers/VMs]
- **Backup strategy:** [Automated backups, retention]

### File Storage
**Decisión:** [Almacenamiento de archivos]
- **Object storage:** [S3, Google Cloud Storage, etc.]
- **CDN integration:** [CloudFront, CloudFlare, etc.]
- **Static assets:** [Build artifacts, media files]

### Secrets Management
**Decisión:** [Gestión de secretos]
- **AWS Secrets Manager** / **Azure Key Vault** / **Google Secret Manager**
- **HashiCorp Vault** / **Kubernetes Secrets**
- **Environment variables:** [12-factor app compliance]

---

## 📊 Monitoring y Observability

### Application Monitoring
**Decisión:** [Herramientas de monitoreo]
- **Prometheus + Grafana** / **DataDog** / **New Relic**
- **AWS CloudWatch** / **Google Cloud Monitoring**

### Logging Strategy
**Decisión:** [Centralización de logs]
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **EFK Stack** (Elasticsearch, Fluentd, Kibana)
- **Cloud-native:** [CloudWatch, Stackdriver, etc.]

### Alerting
**Decisión:** [Sistema de alertas]
- **PagerDuty** / **OpsGenie** / **Slack integrations**
- **Metrics-based:** [CPU, memory, error rates]
- **Log-based:** [Error patterns, anomalies]

### Health Checks
```http
GET /health
{{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0.0",
  "services": {{
    "database": "healthy",
    "redis": "healthy",
    "external_api": "healthy"
  }}
}}
```

---

## 🔧 Configuration Management

### Environment Variables
**Decisión:** [Gestión de configuración]
```bash
# Production environment
NODE_ENV=production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
API_KEY=${SECRET_API_KEY}
```

### Configuration Strategy
**Decisión:** [Estrategia de configuración]
- **12-factor methodology:** [Config in environment]
- **Config maps:** [Kubernetes ConfigMaps]
- **Feature flags:** [External configuration service]

---

## 🔄 Backup y Disaster Recovery

### Backup Strategy
**Decisión:** [Estrategia de respaldo]
- **Database backups:** [Automated, point-in-time]
- **Application data:** [File system, user uploads]
- **Configuration backup:** [IaC templates, secrets]

### Disaster Recovery Plan
**Decisión:** [Plan de recuperación]
- **RTO (Recovery Time Objective):** [Target downtime]
- **RPO (Recovery Point Objective):** [Data loss tolerance]
- **Failover strategy:** [Automated vs manual]
- **Cross-region replication:** [Geographic redundancy]

### Testing DR Procedures
- [ ] **Regular backup verification:** [Restore testing]
- [ ] **Failover testing:** [Quarterly exercises]
- [ ] **Documentation updates:** [Procedure maintenance]

---

## 📈 Scaling Strategy

### Horizontal Scaling
**Decisión:** [Auto-scaling configuration]
- **Metrics-based:** [CPU, memory, request count]
- **Time-based:** [Predictable load patterns]
- **Min/Max instances:** [Resource limits]

### Vertical Scaling
**Decisión:** [Resource optimization]
- **Instance types:** [CPU vs memory optimized]
- **Right-sizing:** [Cost vs performance]
- **Reserved capacity:** [Guaranteed resources]

### Database Scaling
**Decisión:** [Database scaling strategy]
- **Read replicas:** [Read traffic distribution]
- **Sharding:** [Horizontal data partitioning]
- **Connection pooling:** [Resource optimization]

---

## 🔄 Próximos Pasos

### Infrastructure Setup
- [ ] [Configurar cloud provider account]
- [ ] [Setup IaC templates]
- [ ] [Crear environments base]

### CI/CD Implementation
- [ ] [Configurar pipeline básico]
- [ ] [Setup deployment automation]
- [ ] [Implementar testing stages]

### Monitoring y Security
- [ ] [Setup monitoring stack]
- [ ] [Configurar alerting]
- [ ] [Implementar security scanning]

### Production Readiness
- [ ] [Load testing]
- [ ] [Security audit]
- [ ] [Disaster recovery testing]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
