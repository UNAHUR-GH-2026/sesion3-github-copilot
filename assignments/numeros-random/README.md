# 📘 Asignación: Números Random en Python

## 🎯 Objetivo

Aprender a utilizar el módulo `random` de Python para generar números aleatorios y aplicarlos en situaciones prácticas como juegos y simulaciones.

**Conceptos clave:** Módulo `random`, `random.randint()`, `random.choice()`, `random.shuffle()`, simulaciones  
**Nivel de dificultad:** Intermedio  
**Tiempo estimado:** 2-3 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- Variables y tipos de datos en Python
- Bucles (`for`, `while`)
- Condicionales (`if`, `elif`, `else`)
- Funciones definidas con `def`
- Listas y operaciones básicas sobre ellas

## 📝 Tareas

### 🛠️ Generador de Números Aleatorios

#### Descripción
Implementa una función que genere un número entero aleatorio dentro de un rango dado por el usuario y muestre cuántas veces fue necesario intentarlo hasta obtener un número par.

#### Requisitos
El programa completado debe:
- Solicitar al usuario un valor mínimo y un valor máximo para el rango
- Usar `random.randint()` para generar números dentro del rango indicado
- Contar cuántos intentos fueron necesarios hasta obtener un número par
- Mostrar el número generado y la cantidad de intentos realizados

#### Ejemplo de Salida
```
Ingresa el valor mínimo: 1
Ingresa el valor máximo: 20
Generando... intento 1: 7
Generando... intento 2: 13
Generando... intento 3: 4
✅ Número par encontrado: 4 (en 3 intentos)
```

---

### 🛠️ Adivina el Número

#### Descripción
Crea un juego en el que la computadora elige un número aleatorio entre 1 y 100, y el jugador debe adivinarlo. El programa debe dar pistas indicando si el número secreto es mayor o menor que el intento del jugador.

#### Requisitos
El programa completado debe:
- Generar un número secreto aleatorio entre 1 y 100 usando `random.randint()`
- Permitir al jugador ingresar intentos hasta acertar
- Indicar si el número secreto es mayor o menor que el intento
- Contar y mostrar la cantidad de intentos al finalizar
- Mostrar un mensaje de felicitación al adivinar correctamente

#### Ejemplo de Salida
```
🎮 ¡Adivina el número entre 1 y 100!
Tu intento: 50
📈 El número es mayor que 50
Tu intento: 75
📉 El número es menor que 75
Tu intento: 63
🎉 ¡Correcto! Adivinaste en 3 intentos.
```

---

### 🛠️ Simulador de Sorteo (Opcional - Desafío Extra)

#### Descripción
Implementa un simulador de sorteo que reciba una lista de participantes, la mezcle aleatoriamente con `random.shuffle()` y seleccione ganadores usando `random.choice()`.

#### Requisitos
El programa completado debe:
- Recibir una lista de al menos 5 participantes definida en el código
- Mezclar la lista con `random.shuffle()` y mostrar el nuevo orden
- Seleccionar un ganador principal y un suplente usando `random.choice()` sin repetir
- Mostrar los resultados del sorteo con formato claro

#### Ejemplo de Salida
```
Lista original: ['Ana', 'Luis', 'María', 'Juan', 'Sofía']
Lista mezclada: ['María', 'Ana', 'Sofía', 'Juan', 'Luis']
🏆 Ganador principal: Sofía
🥈 Suplente: Juan
```

## 💡 Consejos

- **Consejo 1:** Importa siempre el módulo `random` al inicio del archivo con `import random`.
- **Consejo 2:** Usa `random.randint(a, b)` para obtener un entero aleatorio donde tanto `a` como `b` son inclusivos.
- **Consejo 3:** `random.shuffle()` modifica la lista en el lugar (in-place), no devuelve una lista nueva.

## 🧪 Cómo Probar tu Código

1. Ejecuta el programa y verifica que los números generados caen dentro del rango indicado
2. Juega varias partidas del juego de adivinanza y confirma que las pistas son correctas
3. Corre el simulador de sorteo múltiples veces y verifica que los ganadores cambian entre ejecuciones
4. Prueba con rangos extremos (mínimo igual al máximo) y valida el comportamiento

## 📚 Recursos Adicionales

- [Documentación oficial del módulo `random`](https://docs.python.org/es/3/library/random.html)
- [Tutorial de Python: módulo random](https://docs.python.org/es/3/tutorial/stdlib.html#mathematics)
- [Guía de entrada/salida en Python](https://docs.python.org/es/3/tutorial/inputoutput.html)

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Generador de números aleatorios | 30 pts | Uso correcto de `random.randint()` y lógica de conteo |
| Juego de adivinanza | 40 pts | Flujo del juego, pistas correctas y conteo de intentos |
| Código limpio y comentarios | 20 pts | Código legible, bien organizado y con docstrings |
| Desafío extra (opcional) | 10 pts | Simulador de sorteo con `random.shuffle()` y `random.choice()` |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 14/03/2026
- **Formato:** Archivo `.py` con tu código
- **Nombre del archivo:** `apellido_nombre_numeros_random.py`
- **Instrucciones adicionales:** Asegúrate de que el código ejecute sin errores antes de entregar
