"""
FastAPI con Protección CORS - Código Inicial
API de Gestión de Productos con configuración CORS para distintos entornos.
"""

import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Configuración de la aplicación
# ---------------------------------------------------------------------------

app = FastAPI(
    title="API de Productos con CORS",
    description="API REST con protección CORS configurada para desarrollo y producción",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# TAREA 1: Configurar CORSMiddleware
# ---------------------------------------------------------------------------

# TODO: Leer los orígenes permitidos desde la variable de entorno ALLOWED_ORIGINS.
# Si no está definida, usar "http://localhost:3000" como valor por defecto.
# Pista: usa os.getenv() y str.split(",") para obtener la lista de orígenes.

allowed_origins: List[str] = []  # TODO: Reemplazar con la lógica de la variable de entorno

# TODO: Agregar CORSMiddleware a la aplicación con los siguientes parámetros:
# - allow_origins: la lista de orígenes leída arriba
# - allow_credentials: True
# - allow_methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
# - allow_headers: ["Content-Type", "Authorization"]
# - expose_headers: ["X-Total-Count"]  (Desafío extra)
# - max_age: 600  (Desafío extra)
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=...,
#     ...
# )


# ---------------------------------------------------------------------------
# TAREA 2: Modelos Pydantic
# ---------------------------------------------------------------------------


class ProductCreate(BaseModel):
    """
    Modelo para crear un nuevo producto.

    Attributes:
        name (str): Nombre del producto (mínimo 2 caracteres).
        price (float): Precio del producto (mayor a 0).
        stock (int): Cantidad en stock (mayor o igual a 0).
        category (str): Categoría del producto.
    """

    pass
    # TODO: Definir los campos:
    # - name: str con mínimo 2 caracteres (usa Field con min_length=2)
    # - price: float mayor a 0 (usa Field con gt=0)
    # - stock: int mayor o igual a 0 (usa Field con ge=0)
    # - category: str


class Product(ProductCreate):
    """
    Modelo completo de un producto almacenado.

    Attributes:
        id (int): Identificador único del producto.
    """

    pass
    # TODO: Agregar el campo id: int
    # (hereda name, price, stock, category de ProductCreate)


# ---------------------------------------------------------------------------
# Almacenamiento en memoria (simulación de base de datos)
# ---------------------------------------------------------------------------

products_db: List[Product] = []
next_id = 1


# ---------------------------------------------------------------------------
# TAREA 1 y 3: Endpoints informativos
# ---------------------------------------------------------------------------


@app.get("/")
async def root() -> dict:
    """
    Endpoint raíz con mensaje de bienvenida. (TAREA 1)

    Returns:
        dict: Mensaje de bienvenida con versión y enlace a la documentación.
    """
    pass
    # TODO: Retornar un diccionario con:
    # - "message": "API con protección CORS activa"
    # - "version": "1.0"
    # - "docs": "/docs"


@app.get("/health")
async def health_check() -> dict:
    """
    Endpoint para verificar que la API está en funcionamiento. (TAREA 3)

    Returns:
        dict: Estado de la API.
    """
    pass
    # TODO: Retornar {"status": "ok"}


@app.get("/cors-info")
async def cors_info() -> dict:
    """
    Endpoint que devuelve los orígenes CORS actualmente configurados. (TAREA 3)

    Returns:
        dict: Diccionario con la lista de orígenes permitidos.
    """
    pass
    # TODO: Retornar {"allowed_origins": allowed_origins}


# ---------------------------------------------------------------------------
# TAREA 2: Endpoints CRUD de productos
# ---------------------------------------------------------------------------


@app.post("/products/", status_code=201)
async def create_product(product: ProductCreate) -> Product:
    """
    Crear un nuevo producto en el sistema.

    Parameters:
        product (ProductCreate): Datos del producto a crear.

    Returns:
        Product: El producto creado con su id asignado.
    """
    global next_id
    pass
    # TODO:
    # 1. Crear un Product con id=next_id y los datos de product
    # 2. Agregar a products_db
    # 3. Incrementar next_id
    # 4. Retornar el producto creado


@app.get("/products/")
async def get_products() -> List[Product]:
    """
    Obtener la lista de todos los productos.

    Returns:
        List[Product]: Lista de todos los productos almacenados.
    """
    pass
    # TODO: Retornar products_db


@app.get("/products/{product_id}")
async def get_product(product_id: int) -> Product:
    """
    Obtener un producto por su ID.

    Parameters:
        product_id (int): ID del producto a buscar.

    Returns:
        Product: El producto encontrado.

    Raises:
        HTTPException: 404 si el producto no existe.
    """
    pass
    # TODO:
    # 1. Buscar el producto en products_db por su id
    # 2. Si no existe, lanzar HTTPException con status_code=404
    #    y detail="Producto no encontrado"
    # 3. Retornar el producto


@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int) -> None:
    """
    Eliminar un producto del sistema.

    Parameters:
        product_id (int): ID del producto a eliminar.

    Returns:
        None: Sin contenido (status code 204).

    Raises:
        HTTPException: 404 si el producto no existe.
    """
    global products_db
    pass
    # TODO:
    # 1. Buscar el producto en products_db por su id
    # 2. Si no existe, lanzar HTTPException con status_code=404
    #    y detail="Producto no encontrado"
    # 3. Eliminar el producto de products_db (products_db = [...])
    # 4. No retornar nada (status_code 204)


# ---------------------------------------------------------------------------
# DESAFÍO EXTRA: Búsqueda de productos con header X-Total-Count
# ---------------------------------------------------------------------------


@app.get("/products/search")
async def search_products(
    q: str = Query(..., description="Texto a buscar en el nombre del producto"),
    response: Optional[Response] = None,
) -> List[Product]:
    """
    Buscar productos por nombre.

    Parameters:
        q (str): Texto a buscar en el nombre del producto.
        response (Response): Objeto de respuesta para agregar headers.

    Returns:
        List[Product]: Lista de productos cuyo nombre contiene el texto buscado.
    """
    pass
    # TODO:
    # 1. Filtrar products_db por productos cuyo name contenga q (case-insensitive)
    # 2. Agregar el header X-Total-Count con el total de resultados:
    #    response.headers["X-Total-Count"] = str(len(results))
    # 3. Retornar la lista de resultados filtrados


# Para ejecutar: uvicorn main:app --reload
# Documentación: http://localhost:8000/docs
# Ejemplo con orígenes personalizados:
#   ALLOWED_ORIGINS="https://miapp.com,http://localhost:3000" uvicorn main:app --reload
