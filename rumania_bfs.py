# ------------------------------------------------------------
# Práctica 6 - BFS (Mapa de Rumania)
# Cálculo del tiempo de viaje según hora de inicio
# ------------------------------------------------------------

from collections import deque

# Grafo con distancias base (en minutos sin tráfico)
romania = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# ---------- BFS para encontrar el camino ----------
def bfs_path(graph, start, goal):
    cola = deque([[start]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        ciudad = camino[-1]

        if ciudad == goal:
            return camino

        if ciudad not in visitados:
            visitados.add(ciudad)
            for vecino in graph[ciudad]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None


# ---------- Factor según la hora ----------
def factor_tiempo(hora):
    # 00:00–06:00 = 1.0 | 06:00–16:00 = 2.0 | 16:00–24:00 = 1.5
    if 0 <= hora < 6:
        return 1.0
    elif 6 <= hora < 16:
        return 2.0
    else:
        return 1.5


# ---------- Cálculo del tiempo total ----------
def calcular_tiempo(graph, path, hora_inicio):
    total = 0
    hora_actual = hora_inicio

    print("\n--- Detalle del recorrido ---")
    for i in range(len(path) - 1):
        c1 = path[i]
        c2 = path[i + 1]

        base = graph[c1][c2]
        f = factor_tiempo(hora_actual)
        real = base * f

        total += real
        hora_actual += real / 60  # convertir a horas
        hora_actual %= 24  # reiniciar si pasa de medianoche

        print(f"{c1} → {c2}: {real:.1f} min (hora actual: {hora_actual:.2f})")

    return total


# ---------- Programa principal ----------
if __name__ == "__main__":
    print("=== BFS - Mapa de Rumania ===")

    inicio = input("Ciudad de origen: ").strip().capitalize()
    destino = input("Ciudad destino: ").strip().capitalize()
    try:
        hora = float(input("Hora de inicio (ejemplo: 5.0 para 5:00 am): "))
    except ValueError:
        print("Error: ingresa una hora válida.")
        exit()

    if inicio not in romania or destino not in romania:
        print("Error: una o ambas ciudades no existen en el mapa.")
    else:
        camino = bfs_path(romania, inicio, destino)

        if camino:
            print("\nCamino encontrado:", " → ".join(camino))
            total = calcular_tiempo(romania, camino, hora)
            print(f"\nTiempo total estimado: {total:.1f} minutos")
        else:
            print("No hay camino disponible entre esas ciudades.")