# 📘 Asignación: Rate Limiting con FastAPI

## 🎯 Objetivo

Implementar un sistema de rate limiting (limitación de tasa de peticiones) en una API FastAPI usando la librería `slowapi`, comprendiendo cómo proteger los endpoints de un abuso de uso y cómo comunicar correctamente los límites al cliente.

**Conceptos clave:** Rate Limiting, slowapi, Limiter, headers HTTP, FastAPI, middleware, manejo de errores  
**Nivel de dificultad:** Intermedio  
**Tiempo estimado:** 2-3 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- FastAPI y creación de endpoints REST (tarea anterior: API REST con FastAPI)
- Modelos Pydantic y validación de datos
- Conceptos básicos de HTTP (métodos, headers, códigos de estado)
- Manejo de variables de entorno en Python con `os.getenv()`

## 📝 Tareas

### 🛠️ Configurar el Rate Limiter Global

#### Descripción
Configura `slowapi` en tu aplicación FastAPI para limitar la cantidad de peticiones que un cliente puede hacer en un intervalo de tiempo. El límite global por defecto será de **10 peticiones por minuto** por dirección IP.

#### Requisitos
El programa completado debe:

- Instalar las dependencias con `pip install -r requirements.txt`
- Importar `Limiter` desde `slowapi` y `get_remote_address` desde `slowapi.util`
- Crear una instancia de `Limiter` usando `get_remote_address` como función identificadora de cliente
- Registrar el `Limiter` en el estado de la aplicación (`app.state.limiter`)
- Agregar el `SlowAPIMiddleware` como middleware de la aplicación
- Registrar el manejador de excepción `RateLimitExceeded` con la función `_rate_limit_exceeded_handler`
- Crear un endpoint GET `/` que devuelva un mensaje de bienvenida

#### Ejemplo de Salida
```json
// GET http://localhost:8000/
{
  "message": "API con Rate Limiting activo",
  "version": "1.0",
  "docs": "/docs"
}
```

---

### 🛠️ Implementar Endpoints con Límites Diferenciados

#### Descripción
Crea una API de consulta de artículos que aplique límites distintos según la naturaleza del endpoint: un límite más permisivo para consultas de lectura y uno más estricto para creación de recursos.

#### Requisitos
El programa completado debe:

- Definir un modelo `Article` con Pydantic que incluya: `id` (int), `title` (str, mínimo 3 caracteres), `content` (str, mínimo 10 caracteres), `author` (str)
- Definir un modelo `ArticleCreate` con los campos necesarios para crear un artículo (sin `id`)
- Implementar endpoint GET `/articles/` con límite de **20 peticiones por minuto** usando el decorador `@limiter.limit("20/minute")`
- Implementar endpoint GET `/articles/{article_id}` con límite de **20 peticiones por minuto** que retorne 404 si el artículo no existe
- Implementar endpoint POST `/articles/` con límite de **5 peticiones por minuto** (status code 201) usando el decorador `@limiter.limit("5/minute")`
- Todos los endpoints deben incluir el parámetro `request: Request` requerido por `slowapi`

#### Ejemplo de Salida
```json
// POST http://localhost:8000/articles/
// Body: {"title": "Mi primer artículo", "content": "Contenido del artículo de ejemplo.", "author": "Juan"}
{
  "id": 1,
  "title": "Mi primer artículo",
  "content": "Contenido del artículo de ejemplo.",
  "author": "Juan"
}

// GET http://localhost:8000/articles/
[
  {
    "id": 1,
    "title": "Mi primer artículo",
    "content": "Contenido del artículo de ejemplo.",
    "author": "Juan"
  }
]

// Respuesta cuando se supera el límite (HTTP 429)
{
  "error": "Rate limit exceeded: 5 per 1 minute"
}
```

---

### 🛠️ Configurar Límites desde Variables de Entorno y Endpoint de Estado (Opcional - Desafío Extra)

#### Descripción
Mejora la implementación permitiendo configurar el límite global desde una variable de entorno y agregando un endpoint que informe los límites activos al cliente.

#### Requisitos
El programa completado debe:

- Leer el límite global desde la variable de entorno `RATE_LIMIT` (por ejemplo: `"10/minute"`)
- Si la variable no está definida, usar `"10/minute"` como valor por defecto
- Agregar un endpoint GET `/rate-limit-info` que devuelva el límite global configurado: `{"rate_limit": "10/minute"}`
- Agregar un endpoint GET `/health` que retorne `{"status": "ok"}`
- Aplicar el límite leído de la variable de entorno al endpoint `/rate-limit-info` usando `@limiter.limit(DEFAULT_RATE_LIMIT)`

#### Ejemplo de Salida
```bash
# Variable de entorno configurada
export RATE_LIMIT="20/minute"
```

```json
// GET http://localhost:8000/rate-limit-info
{
  "rate_limit": "20/minute"
}

// GET http://localhost:8000/health
{
  "status": "ok"
}
```

---

## 💡 Consejos

- **Consejo 1:** `slowapi` identifica clientes por IP por defecto usando `get_remote_address`. Cuando desarrollas en local, la IP suele ser `127.0.0.1`, así que todos los intentos cuentan hacia el mismo límite.
- **Consejo 2:** El decorador `@limiter.limit(...)` debe colocarse **antes** del decorador de ruta de FastAPI (`@app.get`, `@app.post`, etc.).
- **Consejo 3:** Cuando se supera el límite, `slowapi` lanza `RateLimitExceeded`. Registra el manejador de error para devolver una respuesta JSON clara con código HTTP 429.
- **Consejo 4:** Todos los endpoints que usen `@limiter.limit(...)` deben recibir el parámetro `request: Request` para que `slowapi` pueda leer la IP del cliente.
- **Consejo 5:** Puedes probar el rate limit rápidamente con un bucle en la terminal: `for i in $(seq 1 10); do curl -s http://localhost:8000/articles/; done`

## 🧪 Cómo Probar tu Código

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el servidor: `uvicorn main:app --reload`
3. Abre tu navegador en `http://localhost:8000/docs` para ver la documentación interactiva
4. Prueba los endpoints con Swagger UI o con `curl`
5. Verifica el rate limit enviando múltiples peticiones rápidas:
   ```bash
   for i in $(seq 1 25); do curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/articles/; done
   ```
6. Verifica que a partir del límite las respuestas devuelven código `429`
7. Configura la variable de entorno y verifica el comportamiento:
   ```bash
   export RATE_LIMIT="5/minute"
   uvicorn main:app --reload
   ```

## 📚 Recursos Adicionales

- [slowapi - Documentación oficial](https://slowapi.readthedocs.io/en/latest/)
- [slowapi en GitHub](https://github.com/laurentS/slowapi)
- [FastAPI - Request Object](https://fastapi.tiangolo.com/advanced/using-request-directly/)
- [HTTP 429 Too Many Requests - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Status/429)

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Configuración del Limiter y middleware | 25 pts | `slowapi` correctamente inicializado y registrado en la app |
| Endpoints de artículos con límites diferenciados | 40 pts | GET y POST con sus respectivos límites y validaciones |
| Manejo del error 429 | 20 pts | Respuesta JSON clara cuando se supera el límite |
| Desafío extra (opcional) | 15 pts | Variable de entorno, `/rate-limit-info` y `/health` implementados |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 04/04/2026
- **Formato:** Archivo `.py` con tu código (main.py) + requirements.txt
- **Nombre del archivo:** `apellido_nombre_fastapi_rate_limit.zip` (incluyendo todos los archivos del proyecto)
- **Instrucciones adicionales:** Incluye un README.txt con instrucciones para ejecutar tu API y las variables de entorno necesarias
