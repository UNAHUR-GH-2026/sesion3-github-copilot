# 📘 Asignación: Autenticación JWT con FastAPI

## 🎯 Objetivo

Implementar un sistema de autenticación seguro usando JSON Web Tokens (JWT) en una API FastAPI, protegiendo endpoints con decoradores y gestionando el ciclo de vida de usuarios (registro y login).

**Conceptos clave:** JWT, Autenticación, OAuth2, Hashing de contraseñas, Endpoints protegidos  
**Nivel de dificultad:** Avanzado  
**Tiempo estimado:** 4-5 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- FastAPI y creación de endpoints REST (tarea anterior: API REST con FastAPI)
- Modelos Pydantic y validación de datos
- Conceptos básicos de seguridad web (autenticación vs. autorización)
- Manejo de excepciones con HTTPException

## 📝 Tareas

### 🛠️ Configurar Registro y Hashing de Contraseñas

#### Descripción
Configura el entorno de autenticación instalando las dependencias necesarias e implementa el endpoint de registro de usuarios. Las contraseñas deben almacenarse de forma segura usando hashing con `bcrypt` a través de la librería `passlib`.

#### Requisitos
El programa completado debe:

- Instalar las dependencias con `pip install -r requirements.txt`
- Definir un modelo `User` con Pydantic que incluya: `id`, `username`, `email`, `hashed_password`, `is_active`
- Definir un modelo `UserCreate` con: `username`, `email`, `password`
- Implementar la función `hash_password(password: str) -> str` que devuelva el hash de la contraseña
- Implementar la función `verify_password(plain: str, hashed: str) -> bool`
- Implementar el endpoint POST `/auth/register` que registre un nuevo usuario
- Retornar error 400 si el nombre de usuario ya existe

#### Ejemplo de Salida
```json
// POST http://localhost:8000/auth/register
// Body: {"username": "estudiante1", "email": "est1@mail.com", "password": "mi_clave_segura"}
{
  "id": 1,
  "username": "estudiante1",
  "email": "est1@mail.com",
  "is_active": true
}
```

---

### 🛠️ Implementar Login y Generación de Tokens JWT

#### Descripción
Implementa el endpoint de login que valida las credenciales del usuario y devuelve un token JWT firmado. El token debe tener un tiempo de expiración configurable y contener el `username` como claim principal.

#### Requisitos
El programa completado debe:

- Definir las constantes `SECRET_KEY`, `ALGORITHM` (HS256) y `ACCESS_TOKEN_EXPIRE_MINUTES`
- Implementar la función `create_access_token(data: dict, expires_delta: Optional[timedelta]) -> str`
- Implementar el endpoint POST `/auth/login` que acepte `username` y `password` (form data)
- Validar credenciales y retornar error 401 si son incorrectas
- Retornar un `access_token` y `token_type: "bearer"` al login exitoso

#### Ejemplo de Salida
```json
// POST http://localhost:8000/auth/login
// Form: username=estudiante1 & password=mi_clave_segura
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

// POST http://localhost:8000/auth/login  (credenciales incorrectas)
{
  "detail": "Usuario o contraseña incorrectos"
}
```

---

### 🛠️ Proteger Endpoints con Dependencias de Autenticación

#### Descripción
Crea una dependencia reutilizable `get_current_user` que valide el token JWT en cada request. Aplica esta dependencia a los endpoints protegidos del módulo de tareas para que solo usuarios autenticados puedan acceder.

#### Requisitos
El programa completado debe:

- Implementar la función `get_current_user(token: str = Depends(oauth2_scheme)) -> User`
- Decodificar y validar el token JWT, lanzando error 401 si el token es inválido o expirado
- Implementar el endpoint GET `/users/me` que devuelva el usuario actualmente autenticado
- Implementar el endpoint GET `/tasks/` protegido que devuelva las tareas del usuario actual
- Implementar el endpoint POST `/tasks/` protegido para crear tareas del usuario autenticado
- Solo el dueño de una tarea debe poder actualizarla o eliminarla (error 403 si otro usuario intenta)

#### Ejemplo de Salida
```json
// GET http://localhost:8000/users/me
// Header: Authorization: Bearer <token>
{
  "id": 1,
  "username": "estudiante1",
  "email": "est1@mail.com",
  "is_active": true
}

// GET http://localhost:8000/tasks/   (sin token)
{
  "detail": "Not authenticated"
}
```

---

### 🛠️ Implementar Refresh Tokens (Opcional - Desafío Extra)

#### Descripción
Extiende el sistema de autenticación implementando refresh tokens de larga duración que permitan renovar el access token sin necesidad de volver a ingresar las credenciales.

#### Requisitos
El programa completado debe:

- Generar un `refresh_token` al hacer login con mayor tiempo de expiración (ej. 7 días)
- Implementar el endpoint POST `/auth/refresh` que acepte un refresh token válido y devuelva un nuevo access token
- Implementar el endpoint POST `/auth/logout` que invalide el refresh token (lista negra en memoria)

## 💡 Consejos

- **Consejo 1:** Usa `Depends()` de FastAPI para inyectar la dependencia `get_current_user` en los endpoints que quieras proteger: `async def endpoint(current_user: User = Depends(get_current_user))`.
- **Consejo 2:** Nunca almacenes contraseñas en texto plano. `passlib` con `bcrypt` es el estándar recomendado: `pwd_context = CryptContext(schemes=["bcrypt"])`.
- **Consejo 3:** Genera un `SECRET_KEY` seguro con `openssl rand -hex 32` y nunca lo expongas en el código fuente en producción.
- **Consejo 4:** Los tokens JWT tienen tres partes: header, payload y signature. El payload contiene los claims (`sub`, `exp`, etc.). Usa `python-jose` para generar y validar tokens.
- **Consejo 5:** El esquema OAuth2 con password flow usa `OAuth2PasswordBearer` y `OAuth2PasswordRequestForm` de FastAPI para manejar el flujo de autenticación estándar.

## 🧪 Cómo Probar tu Código

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el servidor: `uvicorn main:app --reload`
3. Abre `http://localhost:8000/docs` para ver la documentación interactiva
4. Registra un usuario nuevo usando POST `/auth/register`
5. Inicia sesión con POST `/auth/login` y copia el `access_token` recibido
6. En Swagger UI, haz clic en el botón **Authorize** e ingresa `Bearer <token>`
7. Accede a endpoints protegidos como GET `/users/me` y verifica que funcionen
8. Intenta acceder a un endpoint protegido sin token y verifica el error 401

## 📚 Recursos Adicionales

- [Seguridad en FastAPI - Documentación oficial](https://fastapi.tiangolo.com/es/tutorial/security/)
- [OAuth2 con Password y JWT](https://fastapi.tiangolo.com/es/tutorial/security/oauth2-jwt/)
- [python-jose - Librería JWT para Python](https://python-jose.readthedocs.io/en/latest/)
- [passlib - Hashing de contraseñas](https://passlib.readthedocs.io/en/stable/)
- [Introducción a JWT](https://jwt.io/introduction)

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Registro de usuarios | 20 pts | Endpoint funcional con hashing seguro de contraseñas |
| Login y generación de tokens | 25 pts | Token JWT válido con expiración y credenciales verificadas |
| Protección de endpoints | 30 pts | Dependencia `get_current_user` funcionando en rutas protegidas |
| Manejo de errores | 15 pts | Errores 401, 403 y 400 apropiados según el contexto |
| Calidad del código | 10 pts | Código limpio, documentado y con buenas prácticas |
| Desafío extra (opcional) | 10 pts | Refresh tokens implementados correctamente |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 21/03/2026
- **Formato:** Archivo `.py` con tu código (main.py) + requirements.txt
- **Nombre del archivo:** `apellido_nombre_fastapi_jwt_auth.zip` (incluyendo todos los archivos del proyecto)
- **Instrucciones adicionales:** Incluye un README.txt con instrucciones para ejecutar tu API y la SECRET_KEY utilizada para pruebas
