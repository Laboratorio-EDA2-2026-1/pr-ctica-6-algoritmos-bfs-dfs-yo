# -------------------------------------------
# Práctica 6 - Ejercicio 3
# Problema del intervalo 
# -------------------------------------------
def buscar_intervalo(A, q):
    # Caso base: si el arreglo tiene un solo elemento
    if len(A) == 1:
        return A[0], A[0]

    mid = len(A) // 2
    izquierda = A[:mid]
    derecha = A[mid:]

    # Buscamos en ambas mitades
    izq_min, izq_max = buscar_intervalo(izquierda, q) if len(izquierda) > 0 else (float('inf'), float('-inf'))
    der_min, der_max = buscar_intervalo(derecha, q) if len(derecha) > 0 else (float('inf'), float('-inf'))

    # Juntamos todos los valores para revisar
    todos = izquierda + derecha

    # Buscamos el más cercano por debajo y por arriba de q
    menor = None
    mayor = None
    for n in todos:
        if n <= q:
            if menor is None or q - n < q - menor:
                menor = n
        if n >= q:
            if mayor is None or n - q < mayor - q:
                mayor = n

    return menor, mayor


def intervalo_posiciones(A, q):
    menor, mayor = buscar_intervalo(A, q)
    pos1 = A.index(menor) if menor in A else -1
    pos2 = A.index(mayor) if mayor in A else -1
    return [pos1, pos2]


# --- Programa principal ---
if __name__ == "__main__":
    print("=== Problema del intervalo ===")
    A_str = input("Ingrese los valores del arreglo separados por comas: ")
    A = [int(x) for x in A_str.split(",") if x.strip().isdigit()]
    q = float(input("Ingrese el valor de q: "))

    res = intervalo_posiciones(A, q)
    print("\nEl intervalo más pequeño que contiene a q es entre las posiciones:", res)
