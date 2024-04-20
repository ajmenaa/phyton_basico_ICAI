# Programa:Lea un archivo que indique el usuario. 
# Si el archivo no existe. Le notificamos al usuario. 
# Si el archivo existe. Agregamos el texto que indique el usuario

import os

def leer_archivo(nombre_archivo):
    
    try:
        ruta = os.path.join("Estudiantes","Johan_Rojas",nombre_archivo)
        with open('prueba.txt', 'r') as archivo:
            contenido = archivo.read() #El contenido del archivo se asigna
            return contenido
    except FileNotFoundError:
        return ''
    pass

def agregar_archivo(nombre_archivo,texto):
    try:
        ruta = os.path.join("Estudiantes","Johan_Rojas",nombre_archivo)
        with open(ruta, 'w') as archivo:
            archivo.write(texto)
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al crear el archivo: {e}")
    pass

nombre_archivo = input('Ingrese el nombre del archivo a leer: ')
texto_archivo = input('Ingrese el mensaje: ')

#Intentar leer archivo
contenido_leido = leer_archivo(nombre_archivo)

if not contenido_leido:
    print(f"Archivo {nombre_archivo} no existe. Creandolo...")
    agregar_archivo(nombre_archivo,texto_archivo)
    contenido_leido = leer_archivo(nombre_archivo)
    print(f"Contanido agregado: {contenido_leido}")
else:
    print(f"El contenido del archivo{nombre_archivo} es:")
    print(contenido_leido)