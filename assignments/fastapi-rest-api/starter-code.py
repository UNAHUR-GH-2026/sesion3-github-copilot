"""
API REST con FastAPI - Código Inicial
Gestión de Tareas (ToDo List)
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Gestión de Tareas",
    description="API REST para gestionar una lista de tareas",
    version="1.0.0"
)

# TAREA 1: Modelos Pydantic
# Define el modelo Task con los campos necesarios

class Task(BaseModel):
    """
    Modelo para representar una tarea completa.
    
    Attributes:
        id (int): Identificador único de la tarea.
        title (str): Título de la tarea (mínimo 3 caracteres).
        description (Optional[str]): Descripción detallada.
        completed (bool): Estado de completación.
        created_at (datetime): Fecha y hora de creación.
    """
    pass
    # TODO: Agregar campos:
    # - id: int
    # - title: str (mínimo 3 caracteres)
    # - description: Optional[str]
    # - completed: bool = False
    # - created_at: datetime


class TaskCreate(BaseModel):
    """
    Modelo para crear una nueva tarea (sin id ni created_at).
    
    Attributes:
        title (str): Título de la tarea.
        description (Optional[str]): Descripción de la tarea.
        completed (bool): Estado inicial de completación.
    """
    pass
    # TODO: Definir campos necesarios para crear una tarea


class TaskUpdate(BaseModel):
    """
    Modelo para actualizar una tarea existente.
    
    Attributes:
        title (Optional[str]): Nuevo título de la tarea.
        description (Optional[str]): Nueva descripción.
        completed (Optional[bool]): Nuevo estado de completación.
    """
    pass
    # TODO: Todos los campos opcionales


# Almacenamiento en memoria (simulación de base de datos)
tasks_db: List[Task] = []
next_id = 1


# TAREA 1: Ruta de Bienvenida
@app.get("/")
async def root() -> dict:
    """
    Endpoint raíz que da la bienvenida a la API.
    
    Returns:
        dict: Mensaje de bienvenida con información de la API.
    """
    pass
    # TODO: Retornar un diccionario con mensaje de bienvenida,
    # versión y enlace a /docs


# TAREA 2: Crear una nueva tarea (POST)
@app.post("/tasks/", status_code=201)
async def create_task(task: TaskCreate) -> Task:
    """
    Crear una nueva tarea en el sistema.
    
    Parameters:
        task (TaskCreate): Datos de la tarea a crear.
    
    Returns:
        Task: La tarea creada con id y fecha asignados.
    """
    pass
    # TODO:
    # 1. Crear una nueva tarea con id único y fecha actual
    # 2. Agregar a tasks_db
    # 3. Incrementar next_id
    # 4. Retornar la tarea creada


# TAREA 2: Obtener todas las tareas (GET)
@app.get("/tasks/")
async def get_tasks(
    completed: Optional[bool] = Query(
        None,
        description="Filtrar por estado completado"
    ),
    limit: Optional[int] = Query(
        None,
        description="Limitar número de resultados"
    )
) -> List[Task]:
    """
    Obtener lista de tareas con filtros opcionales.
    
    Parameters:
        completed (Optional[bool]): Filtrar por estado completado.
        limit (Optional[int]): Limitar número de resultados.
    
    Returns:
        List[Task]: Lista de tareas que cumplen los filtros.
    """
    pass
    # TODO:
    # 1. Filtrar por completed si se proporciona
    # 2. Aplicar limit si se proporciona
    # 3. Retornar lista de tareas


# TAREA 2: Obtener una tarea específica (GET)
@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> Task:
    """
    Obtener una tarea por su ID.
    
    Parameters:
        task_id (int): ID de la tarea a buscar.
    
    Returns:
        Task: La tarea encontrada.
    
    Raises:
        HTTPException: 404 si la tarea no existe.
    """
    pass
    # TODO:
    # 1. Buscar la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Retornar la tarea


# TAREA 2: Actualizar una tarea (PUT)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task_update: TaskUpdate) -> Task:
    """
    Actualizar una tarea existente.
    
    Parameters:
        task_id (int): ID de la tarea a actualizar.
        task_update (TaskUpdate): Campos a actualizar.
    
    Returns:
        Task: La tarea actualizada.
    
    Raises:
        HTTPException: 404 si la tarea no existe.
    """
    pass
    # TODO:
    # 1. Buscar la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Actualizar solo los campos proporcionados (no None)
    # 4. Retornar la tarea actualizada


# TAREA 2: Eliminar una tarea (DELETE)
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int) -> None:
    """
    Eliminar una tarea del sistema.
    
    Parameters:
        task_id (int): ID de la tarea a eliminar.
    
    Returns:
        None: No retorna contenido (status code 204).
    
    Raises:
        HTTPException: 404 si la tarea no existe.
    """
    pass
    # TODO:
    # 1. Buscar el índice de la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Eliminar la tarea de tasks_db
    # 4. No retornar nada (status_code 204)


# TAREA 3: Estadísticas de tareas (GET)
@app.get("/tasks/stats")
async def get_stats() -> dict:
    """
    Obtener estadísticas de las tareas.
    
    Returns:
        dict: Diccionario con estadísticas (total, completadas,
              pendientes, tasa de completación).
    """
    pass
    # TODO:
    # 1. Calcular total de tareas
    # 2. Calcular tareas completadas
    # 3. Calcular tareas pendientes
    # 4. Calcular tasa de completación
    # 5. Retornar diccionario con las estadísticas


# DESAFÍO EXTRA: Implementar autenticación o persistencia
# - Middleware de autenticación con API Key
# - Guardar/cargar tareas desde archivo JSON
# - Implementar paginación


# Para ejecutar: uvicorn main:app --reload
# Documentación: http://localhost:8000/docs
