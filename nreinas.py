# -----------------------------------------
# Práctica 6 - Ejercicio 1
# N reinas con DFS 
# -----------------------------------------

def se_puede(colocar, fila, col, reinas):
    for c in range(col):
        if reinas[c] == fila or abs(reinas[c] - fila) == abs(c - col):
            return False
    return True

def dfs(N, col, reinas, resultados):
    if col == N:
        resultados.append(reinas[:])
        return
    for fila in range(N):
        if se_puede(reinas, fila, col, reinas):
            reinas[col] = fila
            dfs(N, col + 1, reinas, resultados)

def nreinas(N):
    soluciones = []
    dfs(N, 0, [-1]*N, soluciones)
    return soluciones

# Programa principal
if __name__ == "__main__":
    print("---- Problema de las N Reinas ----")
    N = int(input("Tamaño del tablero (1-8): "))

    if N < 1 or N > 8:
        print("Error: debe estar entre 1 y 8")
    else:
        sols = nreinas(N)
        print("\nTotal de soluciones encontradas:", len(sols))
        for i, s in enumerate(sols):
            print("Solución", i+1, ":", s)
