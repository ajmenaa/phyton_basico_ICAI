import os 

#Programa que lea un archivo que indique el usuario. Si el archivo no existe 
#le notificamos al usuario. Agregamos el texto que indique el usuario

def leer_archivo(nombre_archivo):
    try:
        ruta=os.path.join("Estudiantes","johanhidalgo","Archivos_modulos_paquetes y bibliotecas_01",nombre_archivo)
        with open(ruta,'r') as archivo:
            contenido = archivo.read() #El contenido del archivo se asigna a la variable
            return contenido
    except FileNotFoundError:
        return ''
   

def agregar_archivo(nombre_archivo,texto):
    try:
        ruta = os.path.join("ClassBook","5_Archivos",nombre_archivo)
        with open(ruta, 'w') as archivo:
            archivo.write(texto)
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al crear el archivo: {e}")
    pass

nombre_archivo = input('Ingrese el nombre del archivo a leer')
texto_archivo = input('Ingrese el mensaje')

#Intentar leer el archivo 

contenido_leido =leer_archivo(nombre_archivo)

