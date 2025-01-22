"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    registros={}
    with open("files/input/data.csv", "r" , encoding= "utf-8") as archivo:
        for line in archivo:
            columnas = line.strip().split("\t")
            inicial=columnas[0]
            valor=int(columnas[1])
            if valor in registros:
                registros[valor].append(inicial)
            else:
                registros[valor]=[inicial]
    resultado=[(valor, registros[valor]) for valor in sorted(registros.keys())]
    return resultado

r2=pregunta_07()
print("[")
for tupla in r2:
    print(f"    {tupla},")
print("]")

