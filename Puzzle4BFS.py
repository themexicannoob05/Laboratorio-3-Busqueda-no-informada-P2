import random
from collections import deque as mi_cola


# Función para generar los movimientos posibles (intercambios en este caso)
def obtener_movimientos(posicion_actual):
    movimientos = []
    # Intercambiar dos elementos adyacentes
    for i in range(len(posicion_actual) - 1):
        nuevo_estado = list(posicion_actual)  # Crear copia del estado actual
        nuevo_estado[i], nuevo_estado[i + 1] = nuevo_estado[i + 1], nuevo_estado[i]
        movimientos.append(tuple(nuevo_estado))
    return movimientos


# Función BFS para resolver el puzzle
def bfs(puzzle_inicial, objetivo):
    cola = mi_cola()  # Crear la cola
    cola.append(puzzle_inicial)  # Agregar el estado inicial
    visitados = set()  # Mantener un registro de estados ya visitados

    while cola:
        estado_actual = cola.popleft()  # Obtener el estado actual (FIFO)
        print(f"Visitando estado: {estado_actual}")

        if estado_actual == objetivo:  # Si encontramos la solución
            print("¡Puzzle resuelto!")
            return True

        visitados.add(estado_actual)  # Marcar como visitado

        # Generar y explorar nuevos movimientos
        for nuevo_estado in obtener_movimientos(estado_actual):
            if nuevo_estado not in visitados:  # Evitar estados repetidos
                cola.append(nuevo_estado)

    print("No se encontró solución.")
    return False


# Generar un estado inicial aleatorio
estado_inicial = [1, 2, 3, 4]
random.shuffle(estado_inicial)  # Mezclar los elementos de forma aleatoria
estado_inicial = tuple(estado_inicial)  # Convertir a tupla para que sea inmutable
estado_objetivo = (1, 2, 3, 4)  # Estado objetivo (ordenado)

# Imprimir el estado inicial aleatorio
print(f"Estado inicial aleatorio: {estado_inicial}")

# Resolver el puzzle
bfs(estado_inicial, estado_objetivo)
