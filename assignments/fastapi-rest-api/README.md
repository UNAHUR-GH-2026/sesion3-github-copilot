# 📘 Asignación: API REST con FastAPI

## 🎯 Objetivo

Desarrollar una API REST completa usando FastAPI para gestionar una lista de tareas (ToDo List). Los estudiantes aprenderán a crear endpoints, validar datos, manejar operaciones CRUD y documentar APIs automáticamente.

**Conceptos clave:** APIs REST, FastAPI, HTTP methods (GET, POST, PUT, DELETE), Validación de datos con Pydantic, Documentación automática  
**Nivel de dificultad:** Intermedio/Avanzado  
**Tiempo estimado:** 3-4 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- Fundamentos de Python (clases, diccionarios, listas)
- Conceptos básicos de APIs REST y HTTP
- Programación asíncrona (async/await) - conceptos básicos
- JSON y manipulación de datos
- Uso de pip y gestión de dependencias

## 📝 Tareas

### 🛠️ Configurar el Proyecto y Crear la Primera Ruta

#### Descripción
Configura el entorno de desarrollo con FastAPI y crea tu primera ruta simple. Instala las dependencias necesarias y verifica que el servidor funcione correctamente accediendo a la documentación automática que proporciona FastAPI.

#### Requisitos
El programa completado debe:

- Instalar FastAPI y Uvicorn usando `pip install -r requirements.txt`
- Crear una aplicación FastAPI básica con una ruta raíz (`/`)
- Implementar una ruta GET que devuelva un mensaje de bienvenida
- Ejecutar el servidor con `uvicorn main:app --reload`
- Acceder a la documentación automática en `/docs` y `/redoc`

#### Ejemplo de Salida
```json
// GET http://localhost:8000/
{
  "message": "Bienvenido a la API de Gestión de Tareas",
  "version": "1.0",
  "endpoints": "/docs para ver la documentación"
}
```

---

### 🛠️ Implementar Operaciones CRUD para Tareas

#### Descripción
Crea los endpoints necesarios para gestionar tareas (crear, leer, actualizar y eliminar). Usa modelos Pydantic para validar los datos de entrada y mantén las tareas en memoria (lista en Python).

#### Requisitos
El programa completado debe:

- Definir un modelo `Task` con Pydantic que incluya: `id`, `title`, `description`, `completed` (bool), `created_at`
- Implementar endpoint POST `/tasks/` para crear nuevas tareas
- Implementar endpoint GET `/tasks/` para listar todas las tareas
- Implementar endpoint GET `/tasks/{task_id}` para obtener una tarea específica
- Implementar endpoint PUT `/tasks/{task_id}` para actualizar una tarea
- Implementar endpoint DELETE `/tasks/{task_id}` para eliminar una tarea
- Manejar errores apropiados (404 si no se encuentra la tarea, 422 para validación)

#### Ejemplo de Salida
```json
// POST http://localhost:8000/tasks/
// Body: {"title": "Estudiar FastAPI", "description": "Completar la tarea de FastAPI"}
{
  "id": 1,
  "title": "Estudiar FastAPI",
  "description": "Completar la tarea de FastAPI",
  "completed": false,
  "created_at": "2026-03-07T10:30:00"
}

// GET http://localhost:8000/tasks/
[
  {
    "id": 1,
    "title": "Estudiar FastAPI",
    "description": "Completar la tarea de FastAPI",
    "completed": false,
    "created_at": "2026-03-07T10:30:00"
  }
]
```

---

### 🛠️ Agregar Filtros y Validaciones Avanzadas

#### Descripción
Mejora tu API agregando capacidades de filtrado para las tareas y validaciones más robustas. Implementa query parameters para filtrar tareas por estado y agrega validaciones personalizadas.

#### Requisitos
El programa completado debe:

- Agregar query parameter `completed` en GET `/tasks/` para filtrar por estado
- Implementar query parameter `limit` para limitar el número de resultados
- Validar que el título de la tarea tenga al menos 3 caracteres
- Agregar códigos de estado HTTP apropiados (201 para creación, 204 para eliminación)
- Implementar un endpoint GET `/tasks/stats` que devuelva estadísticas (total, completadas, pendientes)

#### Ejemplo de Salida
```json
// GET http://localhost:8000/tasks/?completed=false&limit=5
[
  {
    "id": 1,
    "title": "Estudiar FastAPI",
    "description": "Completar la tarea de FastAPI",
    "completed": false,
    "created_at": "2026-03-07T10:30:00"
  }
]

// GET http://localhost:8000/tasks/stats
{
  "total": 10,
  "completed": 4,
  "pending": 6,
  "completion_rate": 0.4
}
```

---

### 🛠️ Desafío Extra: Autenticación y Persistencia (Opcional)

#### Descripción
Implementa autenticación básica con tokens y agrega persistencia de datos usando archivos JSON o una base de datos simple (SQLite).

#### Requisitos
El programa completado puede incluir:

- Autenticación mediante API Key en headers
- Middleware para verificar la autenticación en rutas protegidas
- Guardar las tareas en un archivo JSON al crear/modificar/eliminar
- Cargar tareas existentes al iniciar la aplicación
- Implementar paginación para la lista de tareas

## 💡 Consejos

- **Consejo 1:** Usa el decorador `@app.get()`, `@app.post()`, etc. para definir rutas. FastAPI genera automáticamente la documentación basándose en tus tipos de datos.
- **Consejo 2:** Los modelos Pydantic no solo validan datos, sino que también generan automáticamente los esquemas JSON para la documentación. Aprovecha `Field()` para agregar descripciones y validaciones.
- **Consejo 3:** Usa `HTTPException` de FastAPI para manejar errores apropiadamente: `raise HTTPException(status_code=404, detail="Tarea no encontrada")`.
- **Consejo 4:** El flag `--reload` en uvicorn recarga automáticamente el servidor cuando modificas el código, ideal para desarrollo.
- **Consejo 5:** Visita `/docs` en tu navegador para probar tu API interactivamente - FastAPI incluye Swagger UI de forma gratuita.

## 🧪 Cómo Probar tu Código

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el servidor: `uvicorn main:app --reload`
3. Abre tu navegador en `http://localhost:8000/docs` para ver la documentación interactiva
4. Prueba cada endpoint desde la interfaz Swagger UI:
   - Crea varias tareas usando POST
   - Lista todas las tareas con GET
   - Actualiza el estado de una tarea con PUT
   - Elimina una tarea con DELETE
5. Verifica los códigos de estado HTTP y manejo de errores intentando acceder a tareas inexistentes
6. Prueba los filtros y parámetros de consulta

## 📚 Recursos Adicionales

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/es/) - Excelente tutorial en español
- [Tutorial de FastAPI](https://fastapi.tiangolo.com/es/tutorial/) - Guía paso a paso
- [Pydantic - Validación de datos](https://docs.pydantic.dev/) - Documentación de modelos
- [HTTP Status Codes](https://developer.mozilla.org/es/docs/Web/HTTP/Status) - Referencia de códigos de estado
- [REST API Best Practices](https://restfulapi.net/) - Buenas prácticas para diseño de APIs

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Configuración y primera ruta | 15 pts | Servidor funcional con ruta de bienvenida y acceso a /docs |
| Implementación CRUD completa | 35 pts | Todos los endpoints funcionan correctamente con validación |
| Modelos Pydantic correctos | 15 pts | Modelos bien definidos con tipos y validaciones apropiadas |
| Filtros y validaciones avanzadas | 20 pts | Query parameters y endpoint de estadísticas implementado |
| Manejo de errores | 10 pts | Códigos de estado HTTP apropiados y manejo de excepciones |
| Desafío extra (opcional) | 5 pts | Autenticación o persistencia implementada correctamente |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 07/03/2026
- **Formato:** Archivo `.py` con tu código (main.py) + requirements.txt
- **Nombre del archivo:** `apellido_nombre_fastapi_rest_api.zip` (incluyendo todos los archivos del proyecto)
- **Instrucciones adicionales:** Incluye un README.txt con instrucciones para ejecutar tu API y cualquier configuración especial necesaria
