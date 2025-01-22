"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    registros={}
    with open("files/input/data.csv", "r" , encoding= "utf-8") as archivo:
        for line in archivo:
            inicial1 = line.strip().split("\t")[0]
            col5 = line.strip().split("\t")[4]
            val5 = [int(valor.split(":")[1]) for valor in col5.split(",")]
            sumatoria = sum(val5)
            if inicial1 in registros:
                registros[inicial1] += sumatoria
            else:
                registros[inicial1] = sumatoria
    ordenada = dict(sorted(registros.items()))
    return ordenada

print(pregunta_12())
