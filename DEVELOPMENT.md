# 🛠️ Guía de Desarrollo

Esta guía proporciona instrucciones detalladas para configurar el entorno de desarrollo y trabajar con el proyecto localmente.

## 📋 Requisitos del Sistema

### Software Requerido

- **Python:** 3.8 o superior
- **Navegador Web:** Chrome, Firefox, Safari, o Edge (última versión)
- **Editor de Código:** VS Code (recomendado) con GitHub Copilot
- **Git:** 2.x o superior

### Herramientas Opcionales

- **Node.js:** 14+ (para servidor de desarrollo)
- **Python virtualenv:** Para gestión de dependencias
- **Live Server:** Extensión de VS Code para recarga automática

## 🚀 Configuración Inicial

### 1. Clonar el Repositorio

```bash
# Clonar usando HTTPS
git clone https://github.com/unahur/GH-2026/sesion3-github-copilot.git

# O usando SSH
git clone git@github.com:unahur/GH-2026/sesion3-github-copilot.git

# Entrar al directorio
cd sesion3-github-copilot
```

### 2. Configurar Python

#### Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Instalar Dependencias Python

```bash
# Si existe requirements.txt
pip install -r requirements.txt

# Dependencias comunes para las asignaciones
pip install pandas matplotlib numpy jupyter
```

### 3. Configurar el Servidor Web

Necesita un servidor web local para que la interfaz funcione correctamente (debido a fetch de config.json).

#### Opción A: Python HTTP Server (Recomendado)

```bash
# Python 3
python -m http.server 8000

# Abrir en navegador
# http://localhost:8000
```

#### Opción B: Node.js serve

```bash
# Instalar serve globalmente
npm install -g serve

# Ejecutar servidor
serve

# Por defecto usa puerto 3000
# http://localhost:3000
```

#### Opción C: VS Code Live Server

1. Instalar extensión "Live Server" en VS Code
2. Clic derecho en `index.html`
3. Seleccionar "Open with Live Server"

## 🏗️ Estructura de Desarrollo

### Directorios Principales

```
sesion3-github-copilot/
├── assets/              # Recursos estáticos del frontend
│   ├── css/            # Hojas de estilo
│   ├── images/         # Imágenes y gráficos
│   ├── js/             # Scripts JavaScript
│   └── pages/          # Páginas HTML adicionales
├── assignments/         # Asignaciones de Python
├── templates/          # Plantillas reutilizables
├── config.json         # Configuración del curso
└── index.html          # Página principal
```

### Archivos Clave

| Archivo | Propósito | Modificar para... |
|---------|-----------|-------------------|
| `config.json` | Configuración del curso | Agregar/editar asignaciones |
| `index.html` | Página principal | Cambiar estructura HTML |
| `assets/css/styles.css` | Estilos | Cambiar apariencia |
| `assets/js/script.js` | Lógica del portal | Agregar funcionalidad |
| `assets/js/assignment.js` | Página de asignación | Modificar vista de detalle |

## 🔧 Flujo de Trabajo

### Desarrollar una Nueva Asignación

1. **Crear estructura de carpetas:**
```bash
mkdir -p assignments/mi-nueva-asignacion
cd assignments/mi-nueva-asignacion
```

2. **Copiar plantilla:**
```bash
cp ../../templates/assignment-template.md README.md
```

3. **Crear código inicial:**
```bash
# Crear starter-code.py
touch starter-code.py
```

4. **Editar README.md** con los detalles de la asignación

5. **Actualizar config.json:**
```json
{
  "id": "mi-nueva-asignacion",
  "title": "Mi Nueva Asignación",
  "description": "Descripción de la asignación",
  "path": "assignments/mi-nueva-asignacion",
  "dueDate": "2026-04-15",
  "attachments": [
    {
      "name": "Starter Code",
      "file": "starter-code.py",
      "type": "python"
    }
  ]
}
```

6. **Probar:**
   - Actualizar página web
   - Verificar que aparece la nueva asignación
   - Hacer clic para ver el detalle

### Modificar la Interfaz Web

1. **Estilos CSS:**
```css
/* assets/css/styles.css */
.mi-nuevo-estilo {
  /* Agregar estilos aquí */
}
```

2. **JavaScript:**
```javascript
// assets/js/script.js
class AssignmentPortal {
  // Agregar o modificar métodos
  miNuevoMetodo() {
    // Lógica aquí
  }
}
```

3. **Probar cambios:**
   - Refrescar navegador (Ctrl+F5 para limpiar caché)
   - Verificar consola de desarrollador (F12)
   - Probar en diferentes navegadores

### Ejecutar Asignaciones Python

```bash
# Navegar a la carpeta de la asignación
cd assignments/python-basics

# Ejecutar el código inicial
python starter-code.py

# O abrir en Jupyter Notebook
jupyter notebook starter-code.py
```

## 🧪 Testing y Validación

### Validar JSON

```bash
# Usando Python
python -m json.tool config.json

# Verificar salida sin errores
```

### Validar HTML

Usar [W3C Validator](https://validator.w3.org/):
```bash
# O instalar validador local
npm install -g html-validator-cli
html-validator index.html
```

### Validar CSS

```bash
# Instalar stylelint
npm install -g stylelint stylelint-config-standard

# Ejecutar validación
stylelint "assets/css/**/*.css"
```

### Validar JavaScript

```bash
# Instalar ESLint
npm install -g eslint

# Ejecutar validación
eslint assets/js/*.js
```

### Validar Python

```bash
# Instalar herramientas de validación
pip install pylint black flake8

# Ejecutar pylint
pylint assignments/**/*.py

# Formatear con black
black assignments/**/*.py

# Verificar estilo con flake8
flake8 assignments/**/*.py
```

## 🐛 Debugging

### Debugging JavaScript

1. **Abrir DevTools:** F12 o Ctrl+Shift+I
2. **Console:** Ver errores y logs
```javascript
console.log('Debug info:', variable);
console.error('Error:', error);
```

3. **Breakpoints:** Sources → Seleccionar archivo → Clic en número de línea

4. **Network:** Verificar carga de config.json

### Debugging Python

```python
# Usar pdb (Python Debugger)
import pdb

def mi_funcion():
    pdb.set_trace()  # Pausar ejecución aquí
    # Código...
```

**Comandos pdb:**
- `n` (next): Siguiente línea
- `s` (step): Entrar en función
- `c` (continue): Continuar ejecución
- `p variable`: Imprimir valor
- `l` (list): Ver código
- `q` (quit): Salir

### Debugging en VS Code

1. **Crear `.vscode/launch.json`:**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Chrome",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:8000",
      "webRoot": "${workspaceFolder}"
    }
  ]
}
```

2. **Usar breakpoints:** Clic en margen izquierdo del editor
3. **Ejecutar:** F5 o Run → Start Debugging

## 📊 Herramientas de Desarrollo

### Extensiones de VS Code Recomendadas

```json
{
  "recommendations": [
    "github.copilot",
    "github.copilot-chat",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "ritwickdey.liveserver",
    "formulahendry.auto-rename-tag",
    "christian-kohler.path-intellisense"
  ]
}
```

### Configuración de VS Code

Crear `.vscode/settings.json`:
```json
{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "files.associations": {
    "*.json": "jsonc"
  },
  "[python]": {
    "editor.tabSize": 4
  }
}
```

## 🔄 Git Workflow

### Trabajo Diario

```bash
# Actualizar main
git checkout main
git pull origin main

# Crear rama para feature
git checkout -b feat/nueva-caracteristica

# Hacer cambios
# ... editar archivos ...

# Ver cambios
git status
git diff

# Agregar cambios
git add archivo-modificado.py
git add .  # Todos los archivos

# Commit
git commit -m "feat: descripción del cambio"

# Push
git push origin feat/nueva-caracteristica
```

### Sincronizar con Main

```bash
# Estando en su rama
git fetch origin
git rebase origin/main

# Resolver conflictos si es necesario
# git add archivo-resuelto
# git rebase --continue

# Force push si es necesario (solo en su rama)
git push origin feat/nueva-caracteristica --force-with-lease
```

## 📝 Mejores Prácticas

### Código Python

```python
# ✅ Bueno - Claro y documentado
def calculate_grade(score: int, max_score: int = 100) -> str:
    """
    Calcula la calificación basada en el puntaje.
    
    Args:
        score: Puntaje obtenido
        max_score: Puntaje máximo posible
        
    Returns:
        Letra de calificación (A, B, C, D, F)
    """
    percentage = (score / max_score) * 100
    
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# ❌ Malo - Sin documentación, nombres poco claros
def calc(s, m=100):
    p = (s/m)*100
    if p>=90: return "A"
    elif p>=80: return "B"
    elif p>=70: return "C"
    elif p>=60: return "D"
    else: return "F"
```

### Código JavaScript

```javascript
// ✅ Bueno - Async/await, manejo de errores
async function loadAssignments() {
  try {
    const response = await fetch('config.json');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data.assignments;
  } catch (error) {
    console.error('Failed to load assignments:', error);
    throw error;
  }
}

// ❌ Malo - Promises anidados, sin manejo de errores
function loadAssignments() {
  fetch('config.json').then(response => {
    response.json().then(data => {
      return data.assignments;
    });
  });
}
```

## 🆘 Solución de Problemas

### "config.json not found" / CORS Error

**Problema:** El navegador bloquea fetch de archivos locales

**Solución:**
```bash
# Usar servidor HTTP local
python -m http.server 8000
```

### "Module not found" en Python

**Problema:** Falta instalar dependencias

**Solución:**
```bash
pip install nombre-del-modulo
```

### La página no se actualiza

**Problema:** Caché del navegador

**Solución:**
- Hard refresh: Ctrl+F5 (Windows) / Cmd+Shift+R (Mac)
- Abrir DevTools (F12) → Network → Disable cache

### Conflictos de Git

**Problema:** Conflictos al hacer merge/rebase

**Solución:**
```bash
# Ver archivos en conflicto
git status

# Abrir en editor, resolver manualmente
# Buscar: <<<<<<<, =======, >>>>>>>

# Después de resolver
git add archivo-resuelto
git rebase --continue  # o git merge --continue
```

## 📚 Recursos Adicionales

- [Documentación de GitHub Copilot](https://docs.github.com/en/copilot)
- [Python Official Docs](https://docs.python.org/3/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [VS Code Docs](https://code.visualstudio.com/docs)
- [Git Documentation](https://git-scm.com/doc)

## 💬 Soporte

Si encuentra problemas:

1. Verificar esta documentación
2. Buscar en issues existentes
3. Crear un nuevo issue con:
   - Descripción del problema
   - Pasos para reproducir
   - Logs de error
   - Entorno (SO, versión de Python, navegador)

---

**¡Feliz codificación! 🚀**
