# 📋 Documentación de Configuración

Este documento describe la estructura y uso del archivo `config.json` que controla el comportamiento de la interfaz web y las asignaciones del curso.

## 📁 Estructura General

El archivo `config.json` contiene dos secciones principales:

```json
{
  "course": { ... },
  "assignments": [ ... ]
}
```

## 🎓 Sección Course

Define la información general del curso que se muestra en la interfaz web.

### Propiedades

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `title` | string | ✅ Sí | Título del curso (ej: "Computer Science") |
| `school` | string | ✅ Sí | Nombre de la institución educativa |
| `description` | string | ✅ Sí | Descripción breve del curso |

### Ejemplo

```json
{
  "course": {
    "title": "Computer Science",
    "school": "Mergington High School",
    "description": "Introduction to programming and computer science"
  }
}
```

## 📚 Sección Assignments

Un array de objetos que define todas las asignaciones del curso. Cada asignación se renderiza como una tarjeta en la interfaz web.

### Propiedades de Asignación

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `id` | string | ✅ Sí | Identificador único de la asignación (usar kebab-case) |
| `title` | string | ✅ Sí | Título de la asignación visible en la interfaz |
| `description` | string | ✅ Sí | Descripción breve de la asignación |
| `path` | string | ✅ Sí | Ruta relativa a la carpeta de la asignación |
| `dueDate` | string | ✅ Sí | Fecha de vencimiento en formato ISO (YYYY-MM-DD) |
| `attachments` | array | ❌ No | Array de archivos adjuntos a la asignación |

### Propiedades de Attachment

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `name` | string | ✅ Sí | Nombre descriptivo del archivo adjunto |
| `file` | string | ✅ Sí | Nombre del archivo (debe existir en la carpeta de la asignación) |
| `type` | string | ✅ Sí | Tipo de archivo (python, csv, txt, pdf, etc.) |

### Ejemplo de Asignación

```json
{
  "id": "data-analysis",
  "title": "Data Analysis",
  "description": "Basics of data analysis: loading, exploring, and visualizing data in Python.",
  "path": "assignments/data-analysis",
  "dueDate": "2026-03-14",
  "attachments": [
    {
      "name": "Starter Code",
      "file": "starter-code.py",
      "type": "python"
    },
    {
      "name": "Sample Dataset",
      "file": "data.csv",
      "type": "csv"
    }
  ]
}
```

## 🔍 Cómo se Usa la Configuración

### En la Interfaz Web

1. **index.html**: La página principal lee el `config.json` para:
   - Mostrar el título y descripción del curso en el header
   - Listar todas las asignaciones en orden
   - Calcular y destacar la próxima asignación por vencer

2. **assignment.html**: La página de detalle lee:
   - La información de una asignación específica basada en el parámetro `id` de la URL
   - Los archivos adjuntos para mostrar enlaces de descarga

### Algoritmo de "Próxima Asignación"

La interfaz determina la próxima asignación por vencer usando:
1. Filtra asignaciones con fecha futura (después de hoy)
2. Ordena por fecha de vencimiento (más cercana primero)
3. Muestra la primera de la lista

## ➕ Agregar una Nueva Asignación

Para agregar una nueva asignación al sistema:

### 1. Crear la Estructura de Carpetas

```bash
mkdir assignments/nueva-asignacion
```

### 2. Agregar Archivos

Crea al menos:
- `README.md` - Descripción de la asignación
- `starter-code.py` - Código inicial (si aplica)

### 3. Actualizar config.json

Agrega el nuevo objeto al array `assignments`:

```json
{
  "id": "nueva-asignacion",
  "title": "Nueva Asignación",
  "description": "Descripción breve de la nueva asignación",
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

### 4. Validaciones

Asegúrate de que:
- ✅ El `id` sea único
- ✅ El `path` apunte a una carpeta existente
- ✅ La fecha esté en formato ISO correcto
- ✅ Los archivos en `attachments` existan en la carpeta
- ✅ El JSON sea válido (sin comas extras)

## 🎨 Personalización

### Cambiar Fechas de Vencimiento

Simplemente actualiza el campo `dueDate`:

```json
"dueDate": "2026-05-15"
```

### Modificar Información del Curso

Actualiza los campos en la sección `course`:

```json
{
  "course": {
    "title": "Programación Avanzada",
    "school": "Universidad Nacional",
    "description": "Curso avanzado de estructuras de datos y algoritmos"
  }
}
```

### Reorganizar el Orden de las Asignaciones

Las asignaciones se muestran en el orden que aparecen en el array. Para cambiar el orden, mueve los objetos en el JSON.

## ⚠️ Errores Comunes

### Error: "Assignment not found"

**Causa:** El `id` en la URL no coincide con ningún `id` en el config.json  
**Solución:** Verifica que el `id` esté correctamente escrito

### Error: "Failed to load config"

**Causa:** El archivo config.json tiene errores de sintaxis  
**Solución:** Valida el JSON en [jsonlint.com](https://jsonlint.com/)

### Error: Archivo adjunto no se descarga

**Causa:** El archivo especificado en `attachments.file` no existe  
**Solución:** Verifica que el archivo exista en la carpeta especificada en `path`

## 🛠️ Herramientas de Validación

Para validar tu `config.json`:

```bash
# Usando Python
python -m json.tool config.json

# Usando Node.js
node -e "JSON.parse(require('fs').readFileSync('config.json'))"
```

## 📝 Notas Adicionales

- El archivo debe estar codificado en **UTF-8**
- No incluyas comentarios en el JSON (no son válidos)
- Usa comillas dobles `"` para strings, no comillas simples
- Las fechas deben estar en formato **ISO 8601** (YYYY-MM-DD)
- Los IDs deben usar **kebab-case** (minúsculas con guiones)
