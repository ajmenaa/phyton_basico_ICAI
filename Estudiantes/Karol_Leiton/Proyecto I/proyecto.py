import json

# Nombre del archivo JSON
nombre_archivo = "clinica.json"

try:
    # Abrir el archivo JSON y cargar los datos en una estructura de datos adecuada
    with open(nombre_archivo, 'r') as archivo:
        datos_clinica = json.load(archivo)
    
    # Mostrar los datos de la estructura creada
    print("Datos de la clínica:")
    for registro in datos_clinica:
        print(registro)

except FileNotFoundError:
    print(f"No se encontró el archivo {nombre_archivo}. Por favor, asegúrate de que el archivo existe en el directorio correcto.")
except json.JSONDecodeError:
    print(f"El archivo {nombre_archivo} no contiene datos JSON válidos.")
except Exception as e:
    print(f"Se produjo un error: {e}")
