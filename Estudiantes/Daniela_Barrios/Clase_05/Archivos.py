import os

# Programa que lea un archivo que indique el usuario. Si el archivo no está o no existe
#le notificamos al usuario y si sí existe agregamos el texto que indique el usuario

def leer_archivo(nombre_archivo):
    """Función para leer un archivo cuyo nombre recibo de parametro
    
    Args:
    Nombre_archivo (str): nombre del archivo a leer
    """
   
   try:
       ruta = os.path.join("Estudiantes", "Daniela_Barrios", "Clase_05", nombre_archivo)
       with open(ruta, 'r') as archivo:
           contenido = archivo.read() # el contenido del archivo se asigna a la variable
           return contenido
       
   except FileNotFoundError:
       return ""
   

def agregar_texto():
    pass

nombre_archivo = input('Ingrese el nombre del archivo a leer:')
texto_archivo = input('Ingrese el mensaje: ')

#intentar leer archivo

contenido_leido = leer_archivo(nombre_archivo)
print(contenido_leido)

if not contenido_leido:
    print('Archivo no encontrado')
else:
    print(f"el contenido del archivo {nombre_archivo} es: ")
    print(contenido_leido)
    
   