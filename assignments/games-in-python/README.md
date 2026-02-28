# 📘 Asignación: Juego del Ahorcado

## 🎯 Objetivo

Construir el clásico juego de adivinanza de palabras donde los jugadores adivinan letras para revelar una palabra oculta antes de quedarse sin intentos. Este proyecto refuerza el manejo de strings, bucles, condicionales y selección aleatoria en Python.

**Conceptos clave:** Manipulación de strings, bucles, condicionales, selección aleatoria, entrada/salida de usuario  
**Nivel de dificultad:** Intermedio  
**Tiempo estimado:** 2-3 horas

## 📚 Conocimientos Previos

Para completar esta asignación, el estudiante debe estar familiarizado con:
- Variables y tipos de datos en Python
- Bucles (`while`, `for`)
- Condicionales (`if`, `elif`, `else`)
- Funciones y módulo `random`
- Entrada de usuario con `input()`
- Manipulación de strings

## 📝 Tareas

### 🛠️ Crear la Estructura Base del Juego

#### Descripción
Implementa la estructura fundamental del juego del ahorcado. El programa debe seleccionar una palabra aleatoria de una lista predefinida y mantener el control del estado del juego (intento actual, letras adivinadas, intentos restantes).

#### Requisitos
El programa completado debe:
- Importar la palabra de una lista predefinida de al menos 10 palabras
- Mostrar guiones bajos (`_`) para representar letras no adivinadas
- Mantener un contador de intentos disponibles (máximo 6)
- Permitir al jugador ingresar una letra en cada turno
- Validar que la entrada sea una letra única y no se haya adivinado antes

#### Ejemplo de Salida
```
Palabra oculta: _ _ _ _ _
Letras adivinadas: []
Intentos restantes: 6
Adivina una letra: a

Palabra oculta: a _ _ _ _
Letras adivinadas: [a]
Intentos restantes: 6
Adivina una letra: e
```

---

### 🛠️ Implementar Verificación de Letras

#### Descripción
Agrega lógica para verificar si la letra adivinada está en la palabra y actualizar el estado del juego. Si la letra no está en la palabra, decrementa el contador de intentos.

#### Requisitos
El programa completado debe:
- Verificar si la letra está en la palabra oculta
- Mostrar letras adivinadas correctas en sus posiciones
- Decrementar intentos solo si la letra es incorrecta
- Mostrar un mensaje diferente para aciertos y errores
- Evitar contar el mismo error dos veces

#### Ejemplo de Salida
```
Adivina una letra: z
❌ La letra 'z' no está en la palabra.

Adivina una letra: a
✓ ¡Bien! La letra 'a' está en la palabra.
```

---

### 🛠️ Agregar Condiciones de Victoria y Derrota

#### Descripción
Implementa la lógica de fin de juego. El juego termina cuando el jugador adivina la palabra completa o se quedan sin intentos.

#### Requisitos
El programa completado debe:
- Detectar cuando la palabra ha sido completamente adivinada
- Detectar cuando se agotan los intentos
- Mostrar un mensaje de victoria con la palabra
- Mostrar un mensaje de derrota revelando la palabra
- Preguntar si el jugador desea jugar de nuevo

#### Ejemplo de Salida
```
🎉 ¡Felicidades! Adivinaste la palabra: "python"

¿Deseas jugar de nuevo? (s/n): n
Gracias por jugar. ¡Adiós!
```

---

### 🛠️ Desafío Extra: Mejorar la Experiencia (Opcional)

#### Descripción
Agrega características adicionales para mejorar la experiencia del jugador y la complejidad del juego.

#### Requisitos
El programa completado puede incluir:
- Mostrar un dibujo ASCII del ahorcado progresivo
- Agregar categorías de palabras (animales, países, películas)
- Implementar un sistema de puntuación
- Permitir diferentes niveles de dificultad
- Mantener un registro de juegos ganados/perdidos

## 💡 Consejos

- **Consejo 1:** Usa listas para almacenar las palabras disponibles. El módulo `random` puede ayudarte a seleccionar una palabra aleatoria con `random.choice()`.
- **Consejo 2:** Crea una función `mostrar_palabra()` que construya la representación actual de la palabra (con guiones y letras adivinadas).
- **Consejo 3:** Mantén separadas las variables de entrada del usuario de la lógica del juego para facilitar pruebas y modificaciones.
- **Consejo 4:** Usa un conjunto (`set`) para almacenar letras adivinadas - es más eficiente para búsquedas que una lista.

## 🧪 Cómo Probar tu Código

1. Ejecuta el programa y verifica que muestra una palabra oculta y solicita una letra
2. Prueba adivinando letras correctas e incorrectas, y confirma que se actualiza el display
3. Juega hasta ganar completando la palabra antes de agotar intentos
4. Juega hasta perder agotando los intentos sin completar la palabra
5. Verifica que la opción "jugar de nuevo" funciona correctamente

## 📚 Recursos Adicionales

- [Documentación de módulo `random` de Python](https://docs.python.org/es/3/library/random.html)
- [Tutorial de strings en Python](https://docs.python.org/es/3/tutorial/introduction.html#strings)
- [Guía de entrada/salida en Python](https://docs.python.org/es/3/tutorial/inputoutput.html)

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Estructura base y selección de palabra | 25 pts | El juego selecciona palabra aleatoria y muestra display correcto |
| Verificación de letras | 25 pts | Funcionalidad para aciertos, errores y evitar duplicados |
| Condiciones de victoria/derrota | 25 pts | El juego detecta correctamente cuándo gana o pierde |
| Código limpio y comentarios | 15 pts | Código legible, bien organizado y comentado |
| Desafío extra (opcional) | 10 pts | Características adicionales bien implementadas |
| **Total** | **100 pts** | |

## 📤 Entrega

- **Fecha de vencimiento:** 29 de enero, 2026
- **Formato:** Archivo `.py` con tu código
- **Nombre del archivo:** `apellido_nombre_games_in_python.py`
