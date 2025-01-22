"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    registros = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for line in archivo:
            dicc = line.strip().split("\t")[4]
            pares = dicc.split(",")
            for par in pares:
                clave, _ = par.split(":")
                if clave in registros:
                    registros[clave] += 1
                else:
                    registros[clave] = 1
    return registros

resultado = pregunta_09()
print("{")
for clave, valor in resultado.items():
    print(f"    '{clave}': {valor},")
print("}")


