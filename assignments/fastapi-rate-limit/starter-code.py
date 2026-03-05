"""
FastAPI con Rate Limiting - Código Inicial
API de Gestión de Artículos con limitación de tasa de peticiones usando slowapi.
"""

import os
from typing import List

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

# ---------------------------------------------------------------------------
# Configuración del Rate Limiter
# ---------------------------------------------------------------------------

# TODO: Leer el límite global desde la variable de entorno RATE_LIMIT.
# Si no está definida, usar "10/minute" como valor por defecto.
# Pista: usa os.getenv("RATE_LIMIT", "10/minute")

DEFAULT_RATE_LIMIT: str = "10/minute"  # TODO: Reemplazar con la lógica de la variable de entorno

# TODO: Crear una instancia del Limiter usando get_remote_address como
# función identificadora del cliente (key_func).
# Ejemplo: limiter = Limiter(key_func=get_remote_address)

limiter: Limiter  # TODO: Inicializar el Limiter aquí

# ---------------------------------------------------------------------------
# Configuración de la aplicación
# ---------------------------------------------------------------------------

app = FastAPI(
    title="API de Artículos con Rate Limiting",
    description="API REST con limitación de tasa de peticiones usando slowapi",
    version="1.0.0",
)

# TODO: Registrar el limiter en el estado de la aplicación:
#   app.state.limiter = limiter

# TODO: Registrar el manejador de excepción para RateLimitExceeded:
#   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# TODO: Agregar SlowAPIMiddleware a la aplicación:
#   app.add_middleware(SlowAPIMiddleware)


# ---------------------------------------------------------------------------
# TAREA 2: Modelos Pydantic
# ---------------------------------------------------------------------------


class ArticleCreate(BaseModel):
    """
    Modelo para crear un nuevo artículo.

    Attributes:
        title (str): Título del artículo (mínimo 3 caracteres).
        content (str): Contenido del artículo (mínimo 10 caracteres).
        author (str): Nombre del autor del artículo.
    """

    pass
    # TODO: Definir los campos:
    # - title: str con mínimo 3 caracteres (usa Field con min_length=3)
    # - content: str con mínimo 10 caracteres (usa Field con min_length=10)
    # - author: str


class Article(ArticleCreate):
    """
    Modelo completo de un artículo almacenado.

    Attributes:
        id (int): Identificador único del artículo.
    """

    pass
    # TODO: Agregar el campo id: int
    # (hereda title, content y author de ArticleCreate)


# ---------------------------------------------------------------------------
# Almacenamiento en memoria (simulación de base de datos)
# ---------------------------------------------------------------------------

articles_db: List[Article] = []
next_id: int = 1


# ---------------------------------------------------------------------------
# TAREA 1: Endpoints informativos
# ---------------------------------------------------------------------------


@app.get("/")
async def root(request: Request) -> dict:
    """
    Endpoint raíz con mensaje de bienvenida. (TAREA 1)

    Parameters:
        request (Request): Objeto de petición requerido por slowapi.

    Returns:
        dict: Mensaje de bienvenida con versión y enlace a la documentación.
    """
    pass
    # TODO: Retornar un diccionario con:
    # - "message": "API con Rate Limiting activo"
    # - "version": "1.0"
    # - "docs": "/docs"


# ---------------------------------------------------------------------------
# TAREA 2: Endpoints de artículos con límites diferenciados
# ---------------------------------------------------------------------------


# TODO: Aplicar @limiter.limit("20/minute") a este endpoint
@app.get("/articles/")
async def get_articles(request: Request) -> List[Article]:
    """
    Obtener la lista de todos los artículos.
    Límite: 20 peticiones por minuto.

    Parameters:
        request (Request): Objeto de petición requerido por slowapi.

    Returns:
        List[Article]: Lista de todos los artículos almacenados.
    """
    pass
    # TODO: Retornar articles_db


# TODO: Aplicar @limiter.limit("20/minute") a este endpoint
@app.get("/articles/{article_id}")
async def get_article(article_id: int, request: Request) -> Article:
    """
    Obtener un artículo por su ID.
    Límite: 20 peticiones por minuto.

    Parameters:
        article_id (int): ID del artículo a buscar.
        request (Request): Objeto de petición requerido por slowapi.

    Returns:
        Article: El artículo encontrado.

    Raises:
        HTTPException: 404 si el artículo no existe.
    """
    pass
    # TODO:
    # 1. Buscar el artículo en articles_db por su id
    # 2. Si no existe, lanzar HTTPException con status_code=404
    #    y detail="Artículo no encontrado"
    # 3. Retornar el artículo


# TODO: Aplicar @limiter.limit("5/minute") a este endpoint
@app.post("/articles/", status_code=201)
async def create_article(article: ArticleCreate, request: Request) -> Article:
    """
    Crear un nuevo artículo en el sistema.
    Límite: 5 peticiones por minuto.

    Parameters:
        article (ArticleCreate): Datos del artículo a crear.
        request (Request): Objeto de petición requerido por slowapi.

    Returns:
        Article: El artículo creado con su id asignado.
    """
    global next_id
    pass
    # TODO:
    # 1. Crear un Article con id=next_id y los datos de article
    # 2. Agregar a articles_db
    # 3. Incrementar next_id
    # 4. Retornar el artículo creado


# ---------------------------------------------------------------------------
# DESAFÍO EXTRA: Variable de entorno, /rate-limit-info y /health
# ---------------------------------------------------------------------------


@app.get("/rate-limit-info")
async def rate_limit_info(request: Request) -> dict:
    """
    Endpoint que devuelve el límite global de tasa configurado. (Desafío extra)

    Parameters:
        request (Request): Objeto de petición requerido por slowapi.

    Returns:
        dict: Diccionario con el límite global activo.
    """
    pass
    # TODO: Retornar {"rate_limit": DEFAULT_RATE_LIMIT}


@app.get("/health")
async def health_check() -> dict:
    """
    Endpoint para verificar que la API está en funcionamiento. (Desafío extra)

    Returns:
        dict: Estado de la API.
    """
    pass
    # TODO: Retornar {"status": "ok"}


# Para ejecutar: uvicorn main:app --reload
# Documentación: http://localhost:8000/docs
# Ejemplo con límite personalizado:
#   RATE_LIMIT="5/minute" uvicorn main:app --reload
