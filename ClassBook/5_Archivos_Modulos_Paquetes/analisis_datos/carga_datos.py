import random

def generar_lista_compras():
    productos = {
        "manzanas": 1000,
        "bananos": 150,
        "cerezas": 2000,
        "naranjas": 900,
        "pan": 2275,
        "leche": 840,
        "huevos": 3400,
        "queso": 5000
    }
    seleccion = random.sample(list(productos.items()), k=5)  # Selecciona 5 productos aleatorios y los retorna como una lista
    return seleccion

def guardar_lista_compras(lista_compras, nombre_archivo="lista_compras.txt"):
    try:
        # Operaciones con el archivo
        with open(nombre_archivo, 'w') as archivo:
            for producto, precio in lista_compras:
                archivo.write(f"{producto}:{precio}\n")
        print(f"Lista de compras guardada en '{nombre_archivo}'.")
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al trabajar con el archivo: {e}")
    finally:
        if archivo:
            archivo.close()