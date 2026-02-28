"""
Autenticación JWT con FastAPI - Código Inicial
Sistema de registro, login y protección de endpoints con JWT.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field

# ---------------------------------------------------------------------------
# Configuración de la aplicación
# ---------------------------------------------------------------------------

app = FastAPI(
    title="API con Autenticación JWT",
    description="Sistema de autenticación seguro usando JSON Web Tokens",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Configuración de seguridad
# Genera tu propia clave con: openssl rand -hex 32
# ---------------------------------------------------------------------------

SECRET_KEY = "cambia_esta_clave_por_una_segura_en_produccion"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de hashing para contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema OAuth2 para extraer el token del header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# ---------------------------------------------------------------------------
# TAREA 1: Modelos Pydantic
# ---------------------------------------------------------------------------


class UserBase(BaseModel):
    """
    Campos comunes de usuario compartidos entre modelos.

    Attributes:
        username (str): Nombre de usuario único (mínimo 3 caracteres).
        email (str): Dirección de correo electrónico válida.
    """

    username: str = Field(..., min_length=3, description="Nombre de usuario único")
    email: str = Field(..., description="Correo electrónico del usuario")


class UserCreate(UserBase):
    """
    Modelo para registrar un nuevo usuario.

    Attributes:
        password (str): Contraseña en texto plano (mínimo 8 caracteres).
    """

    password: str = Field(..., min_length=8, description="Contraseña del usuario")


class UserResponse(UserBase):
    """
    Modelo de respuesta del usuario (sin datos sensibles).

    Attributes:
        id (int): Identificador único del usuario.
        is_active (bool): Indica si la cuenta está activa.
    """

    id: int
    is_active: bool = True


class UserInDB(UserResponse):
    """
    Representación interna del usuario con contraseña hasheada.

    Attributes:
        hashed_password (str): Contraseña almacenada como hash bcrypt.
    """

    hashed_password: str


class Token(BaseModel):
    """
    Modelo de respuesta para el token de acceso.

    Attributes:
        access_token (str): Token JWT firmado.
        token_type (str): Tipo de token, siempre "bearer".
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Datos extraídos del payload del token JWT.

    Attributes:
        username (Optional[str]): Nombre de usuario codificado en el token.
    """

    username: Optional[str] = None


# ---------------------------------------------------------------------------
# TAREA 2: Modelos para Tareas (reutilizados de la tarea anterior)
# ---------------------------------------------------------------------------


class TaskCreate(BaseModel):
    """
    Modelo para crear una nueva tarea.

    Attributes:
        title (str): Título de la tarea (mínimo 3 caracteres).
        description (Optional[str]): Descripción opcional de la tarea.
    """

    title: str = Field(..., min_length=3, description="Título de la tarea")
    description: Optional[str] = Field(None, description="Descripción opcional")


class Task(TaskCreate):
    """
    Modelo completo de una tarea almacenada.

    Attributes:
        id (int): Identificador único de la tarea.
        completed (bool): Estado de completación de la tarea.
        owner_username (str): Usuario propietario de la tarea.
        created_at (datetime): Fecha y hora de creación.
    """

    id: int
    completed: bool = False
    owner_username: str
    created_at: datetime


# ---------------------------------------------------------------------------
# Almacenamiento en memoria (simulación de base de datos)
# ---------------------------------------------------------------------------

users_db: Dict[str, UserInDB] = {}
tasks_db: List[Task] = []
next_user_id = 1
next_task_id = 1


# ---------------------------------------------------------------------------
# TAREA 1: Funciones de seguridad
# ---------------------------------------------------------------------------


def hash_password(password: str) -> str:
    """
    Genera el hash bcrypt de una contraseña en texto plano.

    Parameters:
        password (str): Contraseña en texto plano a hashear.

    Returns:
        str: Hash bcrypt de la contraseña.
    """
    pass
    # TODO: Usar pwd_context.hash() para generar el hash


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.

    Parameters:
        plain_password (str): Contraseña ingresada por el usuario.
        hashed_password (str): Hash almacenado en la base de datos.

    Returns:
        bool: True si la contraseña es correcta, False en caso contrario.
    """
    pass
    # TODO: Usar pwd_context.verify() para comparar


def get_user(username: str) -> Optional[UserInDB]:
    """
    Busca un usuario en la base de datos por su nombre de usuario.

    Parameters:
        username (str): Nombre de usuario a buscar.

    Returns:
        Optional[UserInDB]: El usuario encontrado o None si no existe.
    """
    pass
    # TODO: Retornar el usuario de users_db si existe


def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    """
    Autentica un usuario verificando su contraseña.

    Parameters:
        username (str): Nombre de usuario.
        password (str): Contraseña en texto plano.

    Returns:
        Optional[UserInDB]: El usuario autenticado o None si las
        credenciales son incorrectas.
    """
    pass
    # TODO:
    # 1. Obtener el usuario con get_user()
    # 2. Si no existe, retornar None
    # 3. Verificar la contraseña con verify_password()
    # 4. Si no coincide, retornar None
    # 5. Retornar el usuario


# ---------------------------------------------------------------------------
# TAREA 2: Función para crear tokens JWT
# ---------------------------------------------------------------------------


def create_access_token(
    data: dict, expires_delta: Optional[timedelta] = None
) -> str:
    """
    Genera un token JWT firmado con los datos proporcionados.

    Parameters:
        data (dict): Datos a codificar en el payload del token.
        expires_delta (Optional[timedelta]): Tiempo de expiración del token.
            Si no se proporciona, usa ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: Token JWT firmado como string.
    """
    pass
    # TODO:
    # 1. Copiar los datos recibidos
    # 2. Calcular la fecha de expiración (now + expires_delta)
    # 3. Agregar "exp" al payload
    # 4. Usar jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    # 5. Retornar el token generado


# ---------------------------------------------------------------------------
# TAREA 3: Dependencia de autenticación
# ---------------------------------------------------------------------------


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    """
    Dependencia de FastAPI que valida el token JWT y retorna el usuario actual.

    Parameters:
        token (str): Token JWT extraído del header Authorization.

    Returns:
        UserInDB: El usuario autenticado.

    Raises:
        HTTPException: 401 si el token es inválido, expirado o el usuario
        no existe.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    pass
    # TODO:
    # 1. Decodificar el token con jwt.decode(token, SECRET_KEY, ALGORITHM)
    # 2. Extraer el campo "sub" del payload como username
    # 3. Si username es None, lanzar credentials_exception
    # 4. Buscar el usuario con get_user(username)
    # 5. Si no existe, lanzar credentials_exception
    # 6. Retornar el usuario


# ---------------------------------------------------------------------------
# TAREA 1: Endpoint de registro
# ---------------------------------------------------------------------------


@app.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(user_data: UserCreate) -> UserInDB:
    """
    Registrar un nuevo usuario en el sistema.

    Parameters:
        user_data (UserCreate): Datos del usuario a registrar.

    Returns:
        UserResponse: El usuario creado (sin contraseña).

    Raises:
        HTTPException: 400 si el nombre de usuario ya existe.
    """
    global next_user_id
    pass
    # TODO:
    # 1. Verificar que el username no exista en users_db
    # 2. Hashear la contraseña con hash_password()
    # 3. Crear un UserInDB con los datos y el hash
    # 4. Guardar en users_db con el username como clave
    # 5. Incrementar next_user_id y retornar el usuario creado


# ---------------------------------------------------------------------------
# TAREA 2: Endpoint de login
# ---------------------------------------------------------------------------


@app.post("/auth/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> dict:
    """
    Autenticar un usuario y devolver un token JWT de acceso.

    Parameters:
        form_data (OAuth2PasswordRequestForm): Datos del formulario con
            username y password.

    Returns:
        dict: Diccionario con access_token y token_type.

    Raises:
        HTTPException: 401 si las credenciales son incorrectas.
    """
    pass
    # TODO:
    # 1. Autenticar con authenticate_user()
    # 2. Si falla, lanzar HTTPException 401 "Usuario o contraseña incorrectos"
    # 3. Crear el token con create_access_token({"sub": user.username})
    # 4. Retornar {"access_token": token, "token_type": "bearer"}


# ---------------------------------------------------------------------------
# TAREA 3: Endpoints protegidos
# ---------------------------------------------------------------------------


@app.get("/users/me", response_model=UserResponse)
async def read_current_user(
    current_user: UserInDB = Depends(get_current_user),
) -> UserInDB:
    """
    Obtener el perfil del usuario actualmente autenticado.

    Parameters:
        current_user (UserInDB): Usuario inyectado por la dependencia.

    Returns:
        UserResponse: Datos del usuario autenticado.
    """
    pass
    # TODO: Simplemente retornar current_user


@app.get("/tasks/", response_model=List[Task])
async def get_my_tasks(
    current_user: UserInDB = Depends(get_current_user),
) -> List[Task]:
    """
    Obtener todas las tareas del usuario autenticado.

    Parameters:
        current_user (UserInDB): Usuario inyectado por la dependencia.

    Returns:
        List[Task]: Lista de tareas del usuario actual.
    """
    pass
    # TODO: Filtrar tasks_db por owner_username == current_user.username


@app.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    current_user: UserInDB = Depends(get_current_user),
) -> Task:
    """
    Crear una nueva tarea para el usuario autenticado.

    Parameters:
        task_data (TaskCreate): Datos de la tarea a crear.
        current_user (UserInDB): Usuario inyectado por la dependencia.

    Returns:
        Task: La tarea recién creada.
    """
    global next_task_id
    pass
    # TODO:
    # 1. Crear Task con id, owner_username y created_at=datetime.utcnow()
    # 2. Agregar a tasks_db
    # 3. Incrementar next_task_id
    # 4. Retornar la tarea creada


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user: UserInDB = Depends(get_current_user),
) -> None:
    """
    Eliminar una tarea del usuario autenticado.

    Parameters:
        task_id (int): ID de la tarea a eliminar.
        current_user (UserInDB): Usuario inyectado por la dependencia.

    Returns:
        None: Sin contenido (204 No Content).

    Raises:
        HTTPException: 404 si la tarea no existe.
        HTTPException: 403 si el usuario no es el propietario de la tarea.
    """
    pass
    # TODO:
    # 1. Buscar la tarea en tasks_db por task_id
    # 2. Si no existe, lanzar HTTPException 404
    # 3. Si el owner_username no es el usuario actual, lanzar HTTPException 403
    # 4. Eliminar la tarea de tasks_db


# Para ejecutar: uvicorn main:app --reload
# Documentación: http://localhost:8000/docs
