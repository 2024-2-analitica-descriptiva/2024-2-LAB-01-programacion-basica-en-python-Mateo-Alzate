"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    registros={}
    with open("files/input/data.csv", "r" , encoding= "utf-8") as archivo:
        for line in archivo:
            val2 = int(line.strip().split("\t")[1])
            inicial4 = line.strip().split("\t")[3].split(",")
            for inicial in inicial4:
                if inicial in registros:
                    registros[inicial] += val2
                else:
                    registros[inicial] = val2
    ordenado = dict(sorted(registros.items()))
    return ordenado

resultado = pregunta_11()
print(f"{resultado}")
