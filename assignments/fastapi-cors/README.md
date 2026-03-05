# 📘 Asignación: Protección CORS con FastAPI

## 🎯 Objetivo

Implementar y configurar la protección CORS (Cross-Origin Resource Sharing) en una API FastAPI, comprendiendo por qué es necesaria y cómo configurarla correctamente para distintos entornos (desarrollo y producción).

**Conceptos clave:** CORS, CORSMiddleware, orígenes permitidos, métodos HTTP, headers, FastAPI, seguridad web  
**Nivel de dificultad:** Intermedio  
**Tiempo estimado:** 2-3 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- FastAPI y creación de endpoints REST (tarea anterior: API REST con FastAPI)
- Modelos Pydantic y validación de datos
- Conceptos básicos de HTTP (métodos, headers, códigos de estado)
- Qué es un navegador web y cómo realiza peticiones a servidores

## 📝 Tareas

### 🛠️ Configurar CORS para Desarrollo

#### Descripción
Configura `CORSMiddleware` en tu aplicación FastAPI para permitir solicitudes desde un frontend local durante el desarrollo. Comprende qué significa cada parámetro de configuración y por qué el navegador bloquea las peticiones cross-origin sin esta configuración.

#### Requisitos
El programa completado debe:

- Instalar las dependencias con `pip install -r requirements.txt`
- Importar y agregar `CORSMiddleware` desde `fastapi.middleware.cors`
- Configurar los orígenes permitidos para desarrollo: `http://localhost:3000` y `http://127.0.0.1:3000`
- Permitir los métodos HTTP: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`
- Permitir los headers: `Content-Type`, `Authorization`
- Habilitar `allow_credentials=True` para permitir el envío de cookies
- Crear un endpoint GET `/` que devuelva un mensaje de bienvenida y el origen de la petición

#### Ejemplo de Salida
```json
// GET http://localhost:8000/
{
  "message": "API con protección CORS activa",
  "version": "1.0",
  "docs": "/docs"
}
```

---

### 🛠️ Implementar Endpoints con Control de CORS por Origen

#### Descripción
Crea una mini API de productos que demuestre cómo funcionan los headers CORS en las respuestas. Implementa endpoints CRUD básicos y verifica que los headers `Access-Control-Allow-Origin` aparezcan correctamente en las respuestas cuando se realizan peticiones desde los orígenes permitidos.

#### Requisitos
El programa completado debe:

- Definir un modelo `Product` con Pydantic que incluya: `id`, `name`, `price` (float mayor a 0), `stock` (int mayor o igual a 0), `category`
- Definir un modelo `ProductCreate` con los campos necesarios para crear un producto (sin `id`)
- Implementar endpoint POST `/products/` para crear un nuevo producto (status code 201)
- Implementar endpoint GET `/products/` para listar todos los productos
- Implementar endpoint GET `/products/{product_id}` para obtener un producto específico (404 si no existe)
- Implementar endpoint DELETE `/products/{product_id}` para eliminar un producto (204 si se elimina, 404 si no existe)
- Todos los endpoints deben responder con los headers CORS correctos gracias al middleware configurado

#### Ejemplo de Salida
```json
// POST http://localhost:8000/products/
// Body: {"name": "Laptop", "price": 999.99, "stock": 10, "category": "Electrónica"}
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "stock": 10,
  "category": "Electrónica"
}

// GET http://localhost:8000/products/
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "stock": 10,
    "category": "Electrónica"
  }
]
```

---

### 🛠️ Configurar CORS para Producción y Validar Orígenes

#### Descripción
Mejora la configuración de CORS para soportar múltiples entornos (desarrollo y producción) leyendo los orígenes permitidos desde una variable de entorno. En producción, los orígenes deben estar restringidos explícitamente; en desarrollo se puede usar una lista más permisiva.

#### Requisitos
El programa completado debe:

- Leer los orígenes permitidos desde la variable de entorno `ALLOWED_ORIGINS` (separados por coma)
- Si la variable no está definida, usar como valor por defecto `http://localhost:3000`
- Agregar un endpoint GET `/cors-info` que devuelva la lista de orígenes actualmente configurados
- Verificar que las peticiones desde un origen NO autorizado reciben una respuesta sin el header `Access-Control-Allow-Origin`
- Agregar un endpoint GET `/health` que devuelva el estado de la API: `{"status": "ok"}`

#### Ejemplo de Salida
```bash
# Variable de entorno configurada
export ALLOWED_ORIGINS="https://miapp.com,https://www.miapp.com"
```

```json
// GET http://localhost:8000/cors-info
{
  "allowed_origins": ["https://miapp.com", "https://www.miapp.com"]
}

// GET http://localhost:8000/health
{
  "status": "ok"
}
```

---

### 🛠️ Desafío Extra: Preflight Requests y Headers Personalizados (Opcional)

#### Descripción
Profundiza en el mecanismo de preflight requests que realiza el navegador antes de enviar ciertas solicitudes. Configura el middleware para soportar headers personalizados y analiza las respuestas OPTIONS que genera FastAPI automáticamente.

#### Requisitos
El programa completado puede incluir:

- Configurar `expose_headers` para exponer el header personalizado `X-Total-Count`
- Agregar el header `X-Total-Count` en la respuesta de GET `/products/` con el total de productos
- Configurar `max_age` en el middleware CORS para cachear las respuestas preflight durante 600 segundos
- Implementar un endpoint GET `/products/search` que acepte el query parameter `q` y filtre productos por nombre
- Usar `Response` de FastAPI para agregar headers personalizados a las respuestas

## 💡 Consejos

- **Consejo 1:** CORS no es una protección del servidor, sino una política del navegador. Las peticiones desde herramientas como `curl` o Postman no están limitadas por CORS. Esto es importante para entender por qué probar desde el navegador da resultados distintos.
- **Consejo 2:** El orden de los middlewares importa. Agrega `CORSMiddleware` antes que cualquier otro middleware para que funcione correctamente con todas las rutas.
- **Consejo 3:** Nunca uses `allow_origins=["*"]` junto con `allow_credentials=True` en producción — el navegador lo rechazará. Si necesitas credenciales, debes listar los orígenes explícitamente.
- **Consejo 4:** El método `OPTIONS` se usa en las preflight requests. FastAPI lo maneja automáticamente cuando configuras `CORSMiddleware`, no necesitas definir ese endpoint manualmente.
- **Consejo 5:** Para probar CORS desde el navegador, abre la consola de desarrollador (F12), ve a la pestaña Red (Network) y busca el header `Access-Control-Allow-Origin` en las respuestas.

## 🧪 Cómo Probar tu Código

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el servidor: `uvicorn main:app --reload`
3. Abre tu navegador en `http://localhost:8000/docs` para ver la documentación interactiva
4. Prueba los endpoints de productos con Swagger UI
5. Verifica los headers CORS en las respuestas usando la pestaña **Network** del navegador (F12)
6. Configura la variable de entorno y verifica el comportamiento:
   ```bash
   export ALLOWED_ORIGINS="https://miapp.com,http://localhost:3000"
   uvicorn main:app --reload
   ```
7. Accede a `http://localhost:8000/cors-info` y verifica que los orígenes coinciden

## 📚 Recursos Adicionales

- [CORS en FastAPI - Documentación oficial](https://fastapi.tiangolo.com/es/tutorial/cors/)
- [¿Qué es CORS? - MDN Web Docs](https://developer.mozilla.org/es/docs/Web/HTTP/CORS)
- [CORSMiddleware de Starlette](https://www.starlette.io/middleware/#corsmiddleware)
- [CORS Explained Simply](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers)

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Configuración CORS básica | 25 pts | Middleware correctamente instalado con orígenes, métodos y headers |
| Endpoints CRUD de productos | 35 pts | Todos los endpoints funcionan con validación y códigos de estado |
| Configuración desde variable de entorno | 25 pts | Orígenes leídos de `ALLOWED_ORIGINS` con valor por defecto |
| Endpoint `/cors-info` y `/health` | 10 pts | Endpoints informativos implementados correctamente |
| Desafío extra (opcional) | 5 pts | Headers personalizados y búsqueda implementados |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 28/03/2026
- **Formato:** Archivo `.py` con tu código (main.py) + requirements.txt
- **Nombre del archivo:** `apellido_nombre_fastapi_cors.zip` (incluyendo todos los archivos del proyecto)
- **Instrucciones adicionales:** Incluye un README.txt con instrucciones para ejecutar tu API y las variables de entorno necesarias
