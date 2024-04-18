"""
try:
    archivo = open("archivo.txt", "r")
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
if archivo:
    archivo.close
"""

import os

def leer_archivo(nombre_archivo):
    
    try:
        ruta = os.path.join("Estudiantes","Luis_HM",nombre_archivo)
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return ''

def agregar_archivo(nombre_archivo, texto):
    try:
        ruta = os.path.join("Estudiantes","Luis_HM",nombre_archivo)
        with open(ruta, "w") as archivo:
        

nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
texto_archivo = input("Ingrese el mensaje: ")

contenido_leido = leer_archivo(nombre_archivo)

if not contenido_leido:
    print('Archivo no encontrado')
else:
    print(f"El contenido del archivo {nombre_archivo} es: ")
    print (contenido_leido)