# Programa: lea un archivo que indique el usuario. Control de rrores si el archivo no existe le notificaos al usuario 
# y si el archivo existe agregamos el texto que indique el usuario

def leer_archivo():
    pass

def agregar_texto():
    pass

nombre_archivo = input('ingrese el nombre del archivo a leer:         ')
texto_archivo = input ('Ingrese el mensaje')

#Intentar leer el archivo

leer_archivo

def agregar_archivo(nombre_archivo,texto):
    try:
        ruta = os.path.join("ClassBook","5_Archivos",nombre_archivo)
        with open(ruta, 'w') as archivo:
            archivo.write(texto)
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al crear el archivo: {e}")
    pass