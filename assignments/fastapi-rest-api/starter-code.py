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
    """Modelo para representar una tarea"""
    pass
    # TODO: Agregar campos:
    # - id: int
    # - title: str (mínimo 3 caracteres)
    # - description: Optional[str]
    # - completed: bool = False
    # - created_at: datetime


class TaskCreate(BaseModel):
    """Modelo para crear una nueva tarea (sin id ni created_at)"""
    pass
    # TODO: Definir campos necesarios para crear una tarea


class TaskUpdate(BaseModel):
    """Modelo para actualizar una tarea"""
    pass
    # TODO: Todos los campos opcionales


# Almacenamiento en memoria (simulación de base de datos)
tasks_db: List[Task] = []
next_id = 1


# TAREA 1: Ruta de Bienvenida
@app.get("/")
async def root():
    """
    Endpoint raíz que da la bienvenida a la API
    """
    pass
    # TODO: Retornar un diccionario con mensaje de bienvenida, versión y enlace a /docs


# TAREA 2: Crear una nueva tarea (POST)
@app.post("/tasks/", status_code=201)
async def create_task(task: TaskCreate):
    """
    Crear una nueva tarea
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
    completed: Optional[bool] = Query(None, description="Filtrar por estado completado"),
    limit: Optional[int] = Query(None, description="Limitar número de resultados")
):
    """
    Obtener lista de tareas con filtros opcionales
    """
    pass
    # TODO:
    # 1. Filtrar por completed si se proporciona
    # 2. Aplicar limit si se proporciona
    # 3. Retornar lista de tareas


# TAREA 2: Obtener una tarea específica (GET)
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """
    Obtener una tarea por su ID
    """
    pass
    # TODO:
    # 1. Buscar la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Retornar la tarea


# TAREA 2: Actualizar una tarea (PUT)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task_update: TaskUpdate):
    """
    Actualizar una tarea existente
    """
    pass
    # TODO:
    # 1. Buscar la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Actualizar solo los campos proporcionados (que no sean None)
    # 4. Retornar la tarea actualizada


# TAREA 2: Eliminar una tarea (DELETE)
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """
    Eliminar una tarea
    """
    pass
    # TODO:
    # 1. Buscar el índice de la tarea en tasks_db
    # 2. Si no existe, lanzar HTTPException con status_code=404
    # 3. Eliminar la tarea de tasks_db
    # 4. No retornar nada (status_code 204)


# TAREA 3: Estadísticas de tareas (GET)
@app.get("/tasks/stats")
async def get_stats():
    """
    Obtener estadísticas de las tareas
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
