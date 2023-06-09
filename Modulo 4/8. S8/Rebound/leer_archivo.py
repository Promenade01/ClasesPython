"""
Partiendo de la actividad realizada en el Rebound Exercises, construya una función que lea el
contenido del archivo informacion.dat.
Teniendo como salida lo siguiente:
$ python ejercicio.py
El archivo informacion.dat ya existe, ha sido creado previamente
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
"""


def leer_archivo():
    try:
        with open('informacion.dat', 'r') as file:
            datos = file.readlines()
            print("El archivo informacion.dat ya existe, ha sido creado previamente")
            for linea in datos:
                print(linea.strip())
    except FileNotFoundError:
        print("No se encuentra el archivo.")


leer_archivo()
