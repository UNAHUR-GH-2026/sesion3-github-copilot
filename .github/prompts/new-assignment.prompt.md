---
agent: agent
description: Crear una nueva tarea de programación
argument-hint: nueva-tarea
tools: [execute, read, edit, search, web, agent, todo]
---

# Crear Nueva Tarea de Programación

Tu objetivo es generar una nueva tarea para los estudiantes.

## Paso 1: Recopilar Información de la Tarea

Si el usuario no la proporciona, pregunta sobre qué tratará la tarea.

## Paso 2: Crear Estructura de la Tarea

1. Crea un nuevo directorio en la carpeta `assignments` con un nombre único basado en el tema de la tarea
1. Crea un nuevo archivo en el directorio llamado `README.md` usando la estructura del archivo [assignment-template.md](../../templates/assignment-template.md)
1. Completa los detalles de la tarea en el archivo README
1. (Opcional) Agrega código inicial o archivos adjuntos si la tarea lo necesita - añade estos archivos a la misma carpeta de la tarea

## Paso 3: Actualizar Configuración del Sitio Web

Actualiza la lista de tareas en el archivo de configuración [config.json](../../config.json) para incluir la nueva tarea. Para el campo dueDate, usa la fecha actual más 7 días a menos que se especifique lo contrario.