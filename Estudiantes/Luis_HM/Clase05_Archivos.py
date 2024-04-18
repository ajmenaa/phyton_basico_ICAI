"""
try:
    archivo = open("archivo.txt", "r")
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
if archivo
"""

def leer_archivo(nombre_archivo):
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return ''

def agregar_texto():
    pass

nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
texto_archivo = input("Ingrese el mensaje: ")

contenido_leido = leer_archivo(nombre_archivo)
print(contenido_leido)