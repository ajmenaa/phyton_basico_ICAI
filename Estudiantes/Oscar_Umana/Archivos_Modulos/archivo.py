#programa que lea un archivo que indique el usuario
#Si el archivo no existe le notificamos al usuario
import os

def leer_archivo():
    try: 
        ruta = os.path.join("Estudiantes","Oscar_Umana","Archivos_Modulos", nombre_archivo)
        with open(nombre_archivo,"r") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "" 
def agregar_texto():
    pass

nombre_archivo = input("ingrese el nombre del archivo a leer: ")
texto_archivo = input("ingrese mensaje")

#intentar leer el archivo

contenido_leido= leer_archivo(nombre_archivo)
print(contenido_leido)

if not contenido_leido:
    print("archivo no encontrado")
else:
    print("El contenido del archivo{nombre_archivo} es:")
    print(contenido_leido)


