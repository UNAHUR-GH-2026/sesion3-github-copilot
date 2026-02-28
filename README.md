# 🎓 Personalización de GitHub Copilot

Este repositorio demuestra las capacidades de personalización de GitHub Copilot mediante un sistema completo de gestión de asignaciones educativas. Incluye una interfaz web interactiva y ejercicios prácticos de programación en Python.

## 📋 Descripción General

Este proyecto simula un curso de Ciencias de la Computación para "Mergington High School" con múltiples asignaciones de Python. La interfaz web permite a los estudiantes visualizar sus tareas, fechas de vencimiento y acceder a los materiales del curso de manera organizada.

**Propósito:** Mostrar cómo GitHub Copilot puede personalizar sus sugerencias basándose en el contexto del proyecto, incluyendo:
- Estructura de carpetas y organización del código
- Configuración JSON con información del curso
- Plantillas y patrones de documentación
- Código existente y convenciones del proyecto

## 🏗️ Estructura del Proyecto

```
sesion3-github-copilot/
├── config.json              # Configuración del curso y asignaciones
├── index.html               # Página principal del portal de estudiantes
├── LICENSE                  # Licencia del proyecto
├── README.md               # Documentación principal
├── assets/                 # Recursos estáticos
│   ├── css/
│   │   └── styles.css      # Estilos de la interfaz web
│   ├── images/             # Imágenes y gráficos
│   └── js/
│       ├── script.js       # Lógica de la interfaz web
│       └── assignment.js   # Gestión de asignaciones individuales
│   └── pages/
│       └── assignment.html # Página de detalle de asignación
├── assignments/            # Carpeta de tareas
│   ├── python-basics/      # Fundamentos de Python
│   ├── games-in-python/    # Desarrollo de juegos
│   ├── python-classes/     # Programación orientada a objetos
│   └── data-analysis/      # Análisis de datos
└── templates/
    └── assignment-template.md  # Plantilla para nuevas asignaciones
```

## 🚀 Cómo Empezar

### Prerrequisitos

- **Python 3.8+** para ejecutar las asignaciones
- **Navegador web moderno** para la interfaz
- **GitHub Copilot** (opcional) para aprovechar las sugerencias contextuales

### Ejecutar la Interfaz Web

1. Clone el repositorio:
   ```bash
   git clone https://github.com/unahur/GH-2026/sesion3-github-copilot.git
   cd sesion3-github-copilot
   ```

2. Abra `index.html` en su navegador web, o inicie un servidor local:
   ```bash
   # Usando Python
   python -m http.server 8000
   
   # O usando Node.js
   npx serve
   ```

3. Navegue a `http://localhost:8000` para ver el portal de asignaciones.

### Trabajar en las Asignaciones

Cada asignación incluye:
- **README.md**: Descripción detallada, objetivos y requisitos
- **starter-code.py**: Código inicial para comenzar
- **Archivos de datos**: Datos necesarios para la asignación (cuando aplique)

Para trabajar en una asignación:

```bash
cd assignments/[nombre-de-la-asignacion]
python starter-code.py
```

## 📚 Asignaciones Disponibles

### 1. 📘 Python Basics
**Fecha de vencimiento:** 14 de enero, 2026  
**Temas:** Variables, tipos de datos, condicionales, bucles  
**Habilidades:** Entrada de usuario, formato de strings, operaciones aritméticas, declaraciones condicionales

### 2. 🎮 Games in Python
**Fecha de vencimiento:** 29 de enero, 2026  
**Temas:** Creación de juegos usando Python  
**Habilidades:** Manipulación de strings, bucles, selección aleatoria, lógica de juegos

### 3. 🏛️ Python Classes
**Fecha de vencimiento:** 8 de febrero, 2026  
**Temas:** Definición y uso de clases en Python  
**Habilidades:** Programación orientada a objetos, encapsulación, métodos, atributos

### 4. 📊 Data Analysis
**Fecha de vencimiento:** 14 de marzo, 2026  
**Temas:** Fundamentos de análisis de datos  
**Habilidades:** Carga de datos, exploración, visualización, análisis estadístico

## 🛠️ Personalización

### Agregar Nuevas Asignaciones

1. Cree una nueva carpeta en `assignments/`:
   ```bash
   mkdir assignments/nueva-asignacion
   ```

2. Use la plantilla para crear el README:
   ```bash
   cp templates/assignment-template.md assignments/nueva-asignacion/README.md
   ```

3. Agregue la configuración en `config.json`:
   ```json
   {
     "id": "nueva-asignacion",
     "title": "Título de la Asignación",
     "description": "Descripción breve",
     "path": "assignments/nueva-asignacion",
     "dueDate": "2026-04-01"
   }
   ```

### Modificar el Aspecto Visual

- **Colores y fuentes**: Edite `assets/css/styles.css`
- **Logo e imágenes**: Reemplace archivos en `assets/images/`
- **Información del curso**: Actualice la sección `course` en `config.json`

## 🤖 Uso con GitHub Copilot

Este repositorio está diseñado para demostrar las capacidades de personalización de GitHub Copilot:

1. **Contexto del Proyecto**: Copilot lee `config.json` y entiende la estructura del curso
2. **Plantillas**: Usa `templates/assignment-template.md` para sugerir nuevas asignaciones consistentes
3. **Patrones de Código**: Aprende de `starter-code.py` existentes para sugerir código similar
4. **Comentarios y Documentación**: Genera documentación en el estilo del proyecto (español, con emojis)

### Ejemplos de Uso

- **Crear nueva asignación**: Copilot sugerirá estructura basada en asignaciones existentes
- **Completar código**: Sugerencias contextuales basadas en los archivos `starter-code.py`
- **Escribir tests**: Genera tests siguiendo los patrones del proyecto
- **Documentar funciones**: Crea docstrings consistentes con el estilo del curso

## 📖 Recursos Adicionales

- [Documentación de GitHub Copilot](https://docs.github.com/en/copilot)
- [Personalización de Copilot](https://docs.github.com/en/copilot/customizing-copilot)
- [Python para Principiantes](https://www.python.org/about/gettingstarted/)

## 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](LICENSE).

## 🙋 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el repositorio
2. Cree una rama para su característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit sus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abra un Pull Request

---

**Nota:** Este es un proyecto educativo demostrativo para mostrar las capacidades de personalización de GitHub Copilot en el contexto de un curso de programación.