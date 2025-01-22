"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    registros={}
    with open("files/input/data.csv", "r" , encoding= "utf-8") as archivo:
        for line in archivo:
            columna=line.strip().split("\t")[4]
            columnafinal=columna.split(",")
            for columnas in columnafinal:
                clave=columnas.split(":")[0]
                valor=int(columnas.split(":")[1])
                if clave in registros:
                    registros[clave]["max"]= max(registros[clave]["max"], valor)
                    registros[clave]["min"]= min(registros[clave]["min"], valor)
                else:
                    registros[clave] = {"min" : valor, "max" : valor}
    resultado=[(inicial, valores["min"], valores["max"]) for inicial, valores in sorted(registros.items())]
    return resultado

print(pregunta_06())

