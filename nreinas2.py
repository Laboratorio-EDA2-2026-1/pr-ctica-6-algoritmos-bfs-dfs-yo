# Práctica 6 - Ejercicio 2
# N reinas con posiciones bloqueadas (según el enunciado correcto)

def se_puede2(sol, fila, col, bloqueadas):
    # Revisa si esta posición está bloqueada
    if col < len(bloqueadas) and bloqueadas[col] == fila:
        return False
    # Revisa conflictos con otras reinas
    for c in range(col):
        if sol[c] == fila or abs(sol[c] - fila) == abs(c - col):
            return False
    return True


def dfs2(N, col, sol, bloqueadas, res):
    if col == N:
        res.append(sol[:])
        return
    for fila in range(N):
        if se_puede2(sol, fila, col, bloqueadas):
            sol[col] = fila
            dfs2(N, col + 1, sol, bloqueadas, res)


def nreinas2(N, bloqueadas):
    resultados = []
    dfs2(N, 0, [-1]*N, bloqueadas, resultados)
    return resultados


# Programa principal (modo alumno)
if __name__ == "__main__":
    print("=== N Reinas con posiciones bloqueadas ===")
    N = int(input("Ingrese el tamaño del tablero (1–8): "))
    txt = input("Ingrese las posiciones bloqueadas separadas por comas (ejemplo: 1,3,0,2) o deje vacío: ")

    bloqueadas = []
    if txt.strip() != "":
        for x in txt.split(","):
            if x.strip().isdigit():
                bloqueadas.append(int(x))

    sol = nreinas2(N, bloqueadas)

    if len(sol) > 0:
        print("\nSe encontraron", len(sol), "soluciones:")
        for i, s in enumerate(sol):
            print("Solución", i+1, ":", s)
    else:
        print("No hay soluciones posibles :(")