# 🚀 Quick Start - The Mighty Task

**¡Comenzar en 5 minutos o menos!**

---

## ⚡ **Setup Ultra-Rápido**

```bash
# 1. Navega al directorio
cd the-mighty-task

# 2. Permisos de ejecución
chmod +x scripts/*.py

# 3. Crear primera sesión (¡YA!)
python scripts/generate-daily.py --auto
```

**¡Listo!** Ya tienes tu primera sesión creada. 🎉

---

## 🎯 **Tu Primera Sesión en 3 Pasos**

### **Paso 1: Generar Todo**
```bash
# Crear sesión completa para hoy
TODAY=$(date +%Y-%m-%d)
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "$TODAY"
python scripts/playbook-processor.py --date="$TODAY" --theme="BACKEND-API-SETUP"
```

### **Paso 2: Comenzar a Trabajar**
```bash
# Abrir archivo principal
code daily-work/${TODAY}_BACKEND-API-SETUP/pending-tasks-${TODAY}_BACKEND-API-SETUP.md

# O con tu editor favorito
vim daily-work/${TODAY}_BACKEND-API-SETUP/pending-tasks-${TODAY}_BACKEND-API-SETUP.md
```

### **Paso 3: Al Final del Día**
```bash
# Verificar todo está bien
python scripts/consistency-checker.py --scan-all

# Generar reporte
python scripts/report-generator.py --date="$TODAY" --theme="BACKEND-API-SETUP"
```

---

## ⚡ **Comandos Más Usados**

```bash
# 🆕 Nueva sesión
python scripts/generate-daily.py --theme "TEMA" --date "YYYY-MM-DD"

# 📚 Templates de apoyo
python scripts/playbook-processor.py --date="YYYY-MM-DD" --theme="TEMA"

# ✅ Verificar consistencia
python scripts/consistency-checker.py --scan-all

# 📊 Generar reporte
python scripts/report-generator.py --date="YYYY-MM-DD" --theme="TEMA"

# 📋 Ver temas disponibles
python scripts/generate-daily.py --list-themes
```

---

## 🎨 **Temas Quick Reference**

| **Backend** | **Frontend** | **DevOps** |
|-------------|--------------|------------|
| BACKEND-API-SETUP | FRONTEND-COMPONENTS | DEPLOYMENT-CONFIG |
| BACKEND-ARCHITECTURE | FRONTEND-ARCHITECTURE | DEVOPS-SETUP |
| API-DESIGN | DESIGN-SYSTEM | TESTING-STRATEGY |
| DATABASE-SCHEMA | - | CLI-DEVELOPMENT |
| DATA-MODELING | - | - |

---

## 🗂️ **¿Dónde Está Todo?**

```bash
daily-work/
├── 2025-01-22_TEMA/
│   ├── pending-tasks-2025-01-22_TEMA.md    # ← TU ARCHIVO PRINCIPAL
│   ├── support-docs/                       # ← Templates para completar
│   └── assets/                            # ← Screenshots y logs
├── .tracking.json                         # ← Historial automático
└── ...

reports/                                   # ← Reportes generados
mission-resumes/                          # ← Resúmenes ejecutivos
```

---

## 🔥 **Pro Tips**

### **💡 Automatiza tu flujo diario:**
```bash
# Crea un script personal
cat > start-daily.sh << 'EOF'
#!/bin/bash
TODAY=$(date +%Y-%m-%d)
THEME=${1:-"BACKEND-API-SETUP"}

echo "🚀 Iniciando día: $TODAY - $THEME"
python scripts/generate-daily.py --theme "$THEME" --date "$TODAY"
python scripts/playbook-processor.py --date="$TODAY" --theme="$THEME"
echo "✅ ¡Todo listo! Archivo principal:"
echo "daily-work/${TODAY}_${THEME}/pending-tasks-${TODAY}_${THEME}.md"
EOF

chmod +x start-daily.sh
./start-daily.sh FRONTEND-COMPONENTS
```

### **🔍 Verificación Express:**
```bash
# Un solo comando para verificar todo
alias check-mighty="python scripts/consistency-checker.py --scan-all"
check-mighty
```

### **📈 Reporte Express:**
```bash
# Generar reporte del último día trabajado
LAST_SESSION=$(ls -1 daily-work/ | grep -E '\d{4}-\d{2}-\d{2}_' | tail -1)
if [ "$LAST_SESSION" ]; then
    DATE=$(echo $LAST_SESSION | cut -d'_' -f1)
    THEME=$(echo $LAST_SESSION | cut -d'_' -f2-)
    python scripts/report-generator.py --date="$DATE" --theme="$THEME"
fi
```

---

## 🆘 **SOS - Resolución Rápida**

### **🚨 "No estás en el directorio raíz"**
```bash
# Verifica que estés en la carpeta correcta
ls -la | grep PLAN-COMPLETO.md
# Si no lo ves: cd the-mighty-task
```

### **🚨 "Sesión no encontrada"**
```bash
# Ver qué sesiones existen
ls -la daily-work/
# Crear nueva: python scripts/generate-daily.py --theme="TEMA" --date="HOY"
```

### **🚨 "Playbook no encontrado"**
```bash
# Ver playbooks disponibles
python scripts/playbook-processor.py --list-playbooks
```

### **🚨 "Permission denied"**
```bash
# Arreglar permisos
chmod +x scripts/*.py
```

---

## 📱 **Workflow Típico**

### **🌅 Inicio del Día (2 min)**
```bash
TODAY=$(date +%Y-%m-%d)
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "$TODAY"
python scripts/playbook-processor.py --date="$TODAY" --theme="BACKEND-API-SETUP"
```

### **💼 Durante el Día**
- Trabaja en: `daily-work/FECHA_TEMA/pending-tasks-FECHA_TEMA.md`
- Completa templates en: `support-docs/`
- Guarda evidencias en: `assets/`

### **🌆 Final del Día (1 min)**
```bash
python scripts/consistency-checker.py --scan-all
python scripts/report-generator.py --date="$TODAY" --theme="BACKEND-API-SETUP"
```

---

## 🎪 **Demos Ultra-Rápidos**

### **Demo 1: Primera Sesión**
```bash
python scripts/generate-daily.py --auto
ls -la daily-work/
```

### **Demo 2: Ver Tu Progreso**
```bash
python scripts/consistency-checker.py --scan-all
```

### **Demo 3: Todos los Temas**
```bash
python scripts/generate-daily.py --list-themes
```

---

## 🚀 **¡Ya Estás Listo!**

**Tu primer comando:**
```bash
python scripts/generate-daily.py --theme "BACKEND-API-SETUP"
```

**Para ayuda completa:**
- 📖 Lee: `README.md`
- 📋 Consulta: `PLAN-COMPLETO.md` 
- 🔍 Diagnostica: `python scripts/consistency-checker.py --scan-all`

**¡Comienza tu primera sesión ahora!** 🎯
