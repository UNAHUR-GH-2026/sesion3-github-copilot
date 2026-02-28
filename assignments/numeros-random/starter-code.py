"""
Tarea: Números Random en Python
Módulo: random
Nivel: Intermedio

Instrucciones:
    Completa las funciones marcadas con TODO para resolver cada ejercicio.
    Lee los comentarios y los ejemplos de salida en el README.md antes de comenzar.
"""

import random
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Tarea 1: Generador de Números Aleatorios
# ---------------------------------------------------------------------------

def buscar_numero_par(minimo: int, maximo: int) -> Tuple[int, int]:
    """
    Genera números aleatorios en el rango [minimo, maximo] hasta
    encontrar un número par.

    Parameters:
        minimo (int): Valor mínimo del rango (inclusive).
        maximo (int): Valor máximo del rango (inclusive).

    Returns:
        Tuple[int, int]: El número par encontrado y la cantidad de intentos.
    """
    # TODO: Usar un bucle que genere números aleatorios con random.randint()
    #       hasta encontrar uno par. Llevar la cuenta de intentos.
    intentos = 0
    numero = None

    # TODO: Reemplaza este bloque con tu implementación
    # while ...:
    #     numero = random.randint(minimo, maximo)
    #     intentos += 1
    #     print(f"Generando... intento {intentos}: {numero}")
    #     if ...:
    #         break

    return numero, intentos


# ---------------------------------------------------------------------------
# Tarea 2: Adivina el Número
# ---------------------------------------------------------------------------

def juego_adivina_numero() -> None:
    """
    Juego interactivo donde la computadora elige un número aleatorio entre
    1 y 100 y el jugador debe adivinarlo con pistas de mayor/menor.
    """
    # TODO: Generar el número secreto con random.randint(1, 100)
    numero_secreto = None  # TODO: reemplaza con random.randint(1, 100)
    intentos = 0

    print("🎮 ¡Adivina el número entre 1 y 100!")

    # TODO: Implementar el bucle del juego
    # while True:
    #     intento = int(input("Tu intento: "))
    #     intentos += 1
    #     if intento < numero_secreto:
    #         print(f"📈 El número es mayor que {intento}")
    #     elif intento > numero_secreto:
    #         print(f"📉 El número es menor que {intento}")
    #     else:
    #         print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
    #         break


# ---------------------------------------------------------------------------
# Tarea 3 (Opcional): Simulador de Sorteo
# ---------------------------------------------------------------------------

def simulador_sorteo(participantes: List[str]) -> Tuple[str, str]:
    """
    Mezcla la lista de participantes y selecciona un ganador y un suplente.

    Parameters:
        participantes (List[str]): Lista con los nombres de los participantes.

    Returns:
        Tuple[str, str]: Nombre del ganador principal y del suplente.
    """
    # TODO: Mezclar la lista con random.shuffle() y mostrar el orden nuevo
    # TODO: Seleccionar ganador principal con random.choice()
    # TODO: Eliminar al ganador de la lista antes de elegir el suplente
    # TODO: Seleccionar suplente con random.choice() de la lista restante

    ganador = None   # TODO: reemplaza con random.choice(participantes)
    suplente = None  # TODO: reemplaza con random.choice(lista_sin_ganador)

    return ganador, suplente


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # --- Tarea 1 ---
    print("=== Tarea 1: Generador de Números Aleatorios ===")
    minimo = int(input("Ingresa el valor mínimo: "))
    maximo = int(input("Ingresa el valor máximo: "))
    numero, intentos = buscar_numero_par(minimo, maximo)
    if numero is not None:
        print(f"✅ Número par encontrado: {numero} (en {intentos} intentos)\n")

    # --- Tarea 2 ---
    print("=== Tarea 2: Adivina el Número ===")
    juego_adivina_numero()

    # --- Tarea 3 (Opcional) ---
    print("\n=== Tarea 3: Simulador de Sorteo ===")
    participantes = ["Ana", "Luis", "María", "Juan", "Sofía"]
    print(f"Lista original: {participantes}")
    ganador, suplente = simulador_sorteo(participantes)
    if ganador and suplente:
        print(f"🏆 Ganador principal: {ganador}")
        print(f"🥈 Suplente: {suplente}")
