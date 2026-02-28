# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Este documento proporciona directrices para contribuir de manera efectiva.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Puedo Contribuir](#cómo-puedo-contribuir)
- [Guía de Estilo](#guía-de-estilo)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Estructura del Proyecto](#estructura-del-proyecto)

## 📜 Código de Conducta

Este proyecto sigue los principios de respeto, colaboración y aprendizaje. Se espera que todos los contribuyentes:

- Sean respetuosos y considerados con otros colaboradores
- Acepten críticas constructivas
- Se enfoquen en lo mejor para el proyecto educativo
- Muestren empatía hacia otros miembros de la comunidad

## 🎯 Cómo Puedo Contribuir

### Reportar Bugs

Antes de crear un reporte de bug:
- ✅ Verifica que no exista ya un issue similar
- ✅ Determina qué repositorio corresponde el problema
- ✅ Reúne información sobre el problema

**Formato del Reporte:**
- **Descripción clara** del problema
- **Pasos para reproducir** el comportamiento
- **Comportamiento esperado** vs. comportamiento actual
- **Capturas de pantalla** (si aplica)
- **Entorno:** navegador, sistema operativo, versión de Python

### Sugerir Mejoras

Las sugerencias son bienvenidas para:
- Nuevas asignaciones
- Mejoras a la interfaz web
- Documentación adicional
- Herramientas de desarrollo

**Formato de Sugerencia:**
- **Descripción clara** de la mejora propuesta
- **Justificación:** ¿Por qué es útil?
- **Ejemplos** de uso o implementación
- **Alternativas consideradas**

### Contribuir con Código

#### Tipos de Contribución

1. **Nuevas Asignaciones**
   - Crear ejercicios educativos de Python
   - Agregar datos de muestra
   - Escribir tests

2. **Mejoras a la Interfaz**
   - Diseño responsivo
   - Accesibilidad
   - Nuevas características

3. **Documentación**
   - Mejorar README
   - Tutoriales
   - Comentarios en código

4. **Tests y CI/CD**
   - Tests unitarios
   - Tests de integración
   - Automatización

## 🎨 Guía de Estilo

### Python

Seguimos [PEP 8](https://pep8.org/) con las siguientes especificaciones:

```python
# ✅ CORRECTO
def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numbers (list): Lista de números enteros o flotantes
        
    Returns:
        float: El promedio de los números
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# ❌ INCORRECTO
def CalculateAverage(Numbers):
    if not Numbers:
        return 0
    return sum(Numbers)/len(Numbers)
```

**Convenciones:**
- ✅ 4 espacios para indentación (no tabs)
- ✅ Nombres de funciones en `snake_case`
- ✅ Nombres de clases en `PascalCase`
- ✅ Constantes en `UPPER_SNAKE_CASE`
- ✅ Docstrings para todas las funciones públicas
- ✅ Longitud máxima de línea: 79 caracteres
- ✅ Imports en orden: estándar, terceros, locales

### JavaScript

Seguimos [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript):

```javascript
// ✅ CORRECTO
class AssignmentManager {
  constructor(config) {
    this.config = config;
    this.assignments = [];
  }

  /**
   * Carga todas las asignaciones desde la configuración
   * @returns {Promise<Array>} Array de asignaciones
   */
  async loadAssignments() {
    const response = await fetch(this.config.url);
    this.assignments = await response.json();
    return this.assignments;
  }
}

// ❌ INCORRECTO
class assignment_manager {
  constructor(config) {
    this.config = config
  }
  
  loadAssignments() {
    fetch(this.config.url).then(response => {
      this.assignments = response.json()
    })
  }
}
```

**Convenciones:**
- ✅ 2 espacios para indentación
- ✅ Usar `const` y `let`, nunca `var`
- ✅ Punto y coma al final de las declaraciones
- ✅ Comillas dobles para strings
- ✅ Arrow functions cuando sea apropiado
- ✅ Async/await preferido sobre promises encadenados
- ✅ JSDoc para funciones públicas

### CSS

```css
/* ✅ CORRECTO */
.assignment-card {
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
  border-radius: 8px;
  background-color: var(--color-white);
}

.assignment-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* ❌ INCORRECTO */
.assignment-card{
    display:flex;
    padding:24px;
    background-color:#ffffff;
}
```

**Convenciones:**
- ✅ 2 espacios para indentación
- ✅ Un selector por línea
- ✅ Espacio después de `:` en propiedades
- ✅ Preferir variables CSS para colores y valores reutilizables
- ✅ Nombres de clases en `kebab-case`
- ✅ Orden lógico de propiedades (posicionamiento, box model, tipografía, visual)

### Markdown

```markdown
<!-- ✅ CORRECTO -->
# Título Principal

## Subtítulo

Este es un párrafo con **énfasis** y *cursiva*.

### Lista de Elementos

- Elemento 1
- Elemento 2
  - Sub-elemento 2.1
  - Sub-elemento 2.2

### Código de Ejemplo

\`\`\`python
def hello_world():
    print("Hello, World!")
\`\`\`

<!-- ❌ INCORRECTO -->
#Título Principal
##Subtítulo sin espacio

Este es un párrafo sin estructura clara.
*Lista mal formada
-Elemento sin espacio
```

**Convenciones:**
- ✅ Un espacio después de `#` en encabezados
- ✅ Línea en blanco antes y después de encabezados
- ✅ Usar emojis para mejorar la legibilidad (📘, 🎯, 🛠️)
- ✅ Bloques de código con lenguaje especificado
- ✅ Listas con sangría consistente

### Mensajes de Commit

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# ✅ CORRECTO
feat: agregar asignación de análisis de datos
fix: corregir cálculo de fecha de vencimiento
docs: actualizar README con instrucciones de instalación
style: formatear código según PEP 8
refactor: reorganizar estructura de carpetas
test: agregar tests para AssignmentPortal

# ❌ INCORRECTO
updated files
fix bug
new feature
```

**Formato:**
```
<tipo>(<alcance>): <descripción>

[cuerpo opcional]

[footer opcional]
```

**Tipos:**
- `feat`: Nueva característica
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, punto y coma faltantes, etc.
- `refactor`: Refactorización de código
- `test`: Agregar tests
- `chore`: Mantenimiento

## 🔄 Proceso de Pull Request

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego clone su fork local
git clone https://github.com/TU-USUARIO/sesion3-github-copilot.git
cd sesion3-github-copilot
```

### 2. Crear una Rama

```bash
# Cree una rama desde main
git checkout -b feature/nombre-descriptivo

# Ejemplos de nombres de rama
git checkout -b feat/nueva-asignacion-regex
git checkout -b fix/corregir-formato-fecha
git checkout -b docs/mejorar-readme
```

### 3. Hacer Cambios

- Realice sus cambios siguiendo la guía de estilo
- Haga commits pequeños y lógicos
- Escriba mensajes de commit descriptivos

```bash
# Agregar archivos
git add archivo-modificado.py

# Commit con mensaje descriptivo
git commit -m "feat: agregar función de validación de entrada"
```

### 4. Sincronizar con Upstream

```bash
# Agregar el repositorio original como remote
git remote add upstream https://github.com/unahur/sesion3-github-copilot.git

# Obtener cambios
git fetch upstream

# Integrar cambios
git rebase upstream/main
```

### 5. Push y Crear PR

```bash
# Push a su fork
git push origin feature/nombre-descriptivo
```

Luego:
1. Vaya a GitHub y cree un Pull Request
2. Complete la plantilla de PR
3. Espere la revisión

### Checklist de PR

Antes de enviar, asegúrese de que:

- [ ] El código sigue la guía de estilo del proyecto
- [ ] Los commits siguen el formato de Conventional Commits
- [ ] Ha actualizado la documentación si es necesario
- [ ] Ha agregado tests para nuevas funcionalidades
- [ ] Todos los tests pasan
- [ ] El código no tiene conflictos con la rama main
- [ ] Ha probado manualmente los cambios

## 📁 Estructura del Proyecto

### Agregar una Nueva Asignación

1. **Crear carpeta:**
```bash
mkdir assignments/nueva-asignacion
```

2. **Agregar archivos requeridos:**
```bash
assignments/nueva-asignacion/
├── README.md           # Descripción de la asignación
├── starter-code.py    # Código inicial
└── solution.py        # Solución (opcional, en carpeta separada)
```

3. **Usar la plantilla:**
```bash
cp templates/assignment-template.md assignments/nueva-asignacion/README.md
```

4. **Actualizar config.json:**
```json
{
  "id": "nueva-asignacion",
  "title": "Título de la Asignación",
  "description": "Descripción breve",
  "path": "assignments/nueva-asignacion",
  "dueDate": "2026-04-01",
  "attachments": [
    {
      "name": "Starter Code",
      "file": "starter-code.py",
      "type": "python"
    }
  ]
}
```

5. **Validar:**
```bash
# Validar JSON
python -m json.tool config.json

# Verificar que los archivos existen
ls -la assignments/nueva-asignacion
```

### Modificar la Interfaz Web

```
assets/
├── css/
│   └── styles.css      # Modificar estilos aquí
├── js/
│   ├── script.js       # Lógica principal del portal
│   └── assignment.js   # Lógica de página de asignación
└── pages/
    └── assignment.html # Plantilla de página de asignación
```

## 🧪 Tests

Aunque actualmente el proyecto no tiene tests automatizados, se espera que las contribuciones incluyan:

### Python
```python
# tests/test_assignment.py
import pytest
from assignments.python_basics import starter_code

def test_welcome_message():
    # TODO: Implementar tests
    pass
```

### JavaScript
```javascript
// tests/portal.test.js
describe('AssignmentPortal', () => {
  test('should load configuration', async () => {
    // TODO: Implementar tests
  });
});
```

## 💡 Consejos para Contribuir

1. **Comience pequeño:** Arregle un typo, mejore la documentación
2. **Comuníquese:** Abra un issue antes de trabajar en cambios grandes
3. **Sea paciente:** La revisión puede tomar tiempo
4. **Aprenda:** Use GitHub Copilot para mejorar su código
5. **Contribuya regularmente:** Las pequeñas contribuciones consistentes son valiosas

## 📞 Contacto

Si tiene preguntas:
- Abra un issue en GitHub
- Consulte la documentación existente
- Revise issues cerrados para problemas similares

## 🙏 Agradecimientos

¡Gracias por contribuir al aprendizaje de programación! Cada contribución hace que este recurso sea mejor para estudiantes en todo el mundo.

---

**Recuerde:** Este es un proyecto educativo. El objetivo es ayudar a los estudiantes a aprender programación con GitHub Copilot como herramienta de apoyo.
