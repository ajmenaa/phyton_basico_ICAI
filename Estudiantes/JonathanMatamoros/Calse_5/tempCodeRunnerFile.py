import pandas as pd

# Crear un diccionario de Python con datos de estudiantes
datos = {
    "Nombre": ["Juan", "Maria", "Pedro", "Ana"],
    "Edad": [20, 22, 18, 21],
    "Nota": [85, 92, 78, 90]
}

# Crear un DataFrame de Pandas a partir del diccionario
dataframe = pd.DataFrame(datos)

# Imprimir el DataFrame completo
print(dataframe)

# Acceder a una columna específica (por nombre)
edades = dataframe["Edad"]
print(f"\nEdades: {edades}")

# Obtener estadísticas descriptivas de una columna
print(dataframe["Nota"].describe())

# Filtrar filas por condición
mayores_edad = dataframe[dataframe["Edad"] >= 18]
print(f"\nMayores de edad:\n{mayores_edad}")

# Crear una columna nueva a partir de otra
dataframe["Aprobado"] = dataframe["Nota"] >= 70
print(f"\nCon columna 'Aprobado':\n{dataframe}")