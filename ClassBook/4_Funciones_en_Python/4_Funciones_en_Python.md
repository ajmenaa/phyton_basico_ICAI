# Funciones en Python: Definición, Ejemplos y Documentación

## Introducción
Las funciones en Python son bloques de código reutilizables que permiten modularizar el programa, mejorar la legibilidad y evitar la duplicación de código. Se definen utilizando la palabra clave **def** seguida del nombre de la función, paréntesis, parámetros opcionales y dos puntos. A continuación, se escribe el bloque de código indentado que representa el cuerpo de la función.

## Estructura de una función


```python
def nombre_funcion(parametro1, parametro2):
  """
  Documentación de la función

  Esta función realiza ...

  Parámetros:
    parametro1: Descripción del primer parámetro.
    parametro2: Descripción del segundo parámetro.
    ...

  Retorno:
    Valor de retorno de la función (opcional).
  """
  # Bloque de código de la función
  ...
```

### Características
- **Reutilizables:** Las funciones se pueden llamar desde cualquier parte del programa.
- **Modulares:** Permiten dividir el programa en secciones más pequeñas y manejables.
- **Legibles:** Mejoran la comprensión del código al agru
par funcionalidades relacionadas.
- **Evitar duplicación:** Eliminan la necesidad de escribir el mismo código varias veces.

## Ejemplos

#### 1. Función para saludar:º


```python
def saludar(nombre):
  """
  Función que saluda a una persona por su nombre.

  Parámetro:
    nombre: El nombre de la persona a saludar.

  Retorno:
    Un mensaje de saludo personalizado.
  """
  mensaje = "Hola " + nombre + "! ¿Cómo estás?"
  return mensaje

# Llamada a la función
persona = "Andrés"
saludo = saludar(persona)
print(saludo)
```

    Hola Andrés! ¿Cómo estás?
    

#### 2. Función con parámetros por defecto y valores de retorno múltiples:


```python
def calcular_area_y_perimetro_rectangulo(base, altura, unidad="cm"):
  """
  Función para calcular el área y perímetro de un rectángulo.

  Parámetros:
    base: La longitud de la base del rectángulo (obligatorio).
    altura: La longitud de la altura del rectángulo (obligatorio).
    unidad: La unidad de medida para el área y perímetro (opcional, por defecto "cm").

  Retorno:
    Una tupla con el área y perímetro del rectángulo, en la unidad especificada.
  """
  area = base * altura
  perimetro = 2 * (base + altura)
  return area, perimetro, unidad

# Llamada a la función con parámetros por defecto
resultado = calcular_area_y_perimetro_rectangulo(5, 3)
print("Área:", resultado[0], resultado[2])  # Acceder al área y unidad
print("Perímetro:", resultado[1], resultado[2])  # Acceder al perímetro y unidad

# Llamada a la función con todos los parámetros
resultado = calcular_area_y_perimetro_rectangulo(10, 7, "m")
print("Área (en metros):", resultado[0], resultado[2])
print("Perímetro (en metros):", resultado[1], resultado[2])
```

    Resultado: 100
    Suma: 10
    Resultado: 512
    Suma: 8
    

**Explicación:**

1. La función calcular_area_y_perimetro_rectangulo toma dos parámetros obligatorios, base y altura, y un parámetro opcional unidad con valor por defecto "cm".
2. La función calcula el área y perímetro del rectángulo utilizando las fórmulas:
*área = base * altura y perímetro = 2 * (base + altura)*.
3. La función retorna una tupla que contiene tres elementos: el área, el perímetro y la unidad de medida.
4. Al llamar a la función, se pueden especificar los valores para todos los parámetros o solo para algunos. Si no se especifica un valor para un parámetro opcional, se utiliza el valor por defecto.
5. En la tupla de retorno, cada elemento se puede acceder por su índice: resultado[0] para el área, resultado[1] para el perímetro y resultado[2] para la unidad.

#### 3. Función para contar la cantidad de vocales en una cadena:


```python
#Programa contar vocales en 5 frases
def contar_vocales(cadena,activa_mayus=False):
  if activa_mayus:
    vocales = 'aeiouAEIOU'
  else:
    vocales = 'aeiou'

  contador_vocales = 0

  for letra in cadena:
    if letra in vocales:
      contador_vocales += 1 # contador_vocales = contador_vocals + 1
  return contador_vocales

contador = 0
while contador <=5:
  frase = input('Ingrese la frase: ')
  #contar_vocales
  cantidad_vocales = contar_vocales(frase,True)
  print(f'La frase {frase} contiene {cantidad_vocales} vocales')
  contador += 1
```

### Calcular promedios de estudiantes
**Descripción del problema:**

Un profesor necesita calcular el promedio de calificaciones de sus estudiantes en un curso. Cada estudiante tiene una sola calificación. El profesor desea crear un programa que le permita:

1. Ingresar las calificaciones de cada estudiante.
2. Calcular el promedio general de la clase.
3. Mostrar una tabla con los nombres de los estudiantes y sus calificaciones.


**Solución utilizando ciclos y funciones:**


```python
def calcular_promedio(calificaciones):
  """
  Función para calcular el promedio de una lista de calificaciones.

  Parámetro:
    calificaciones: Una lista de calificaciones numéricas.

  Retorno:
    El promedio de las calificaciones.
  """
  suma_calificaciones = 0
  for calificacion in calificaciones:
    suma_calificaciones += calificacion
  promedio = suma_calificaciones / len(calificaciones)
  return promedio

def mostrar_tabla_resultados(estudiantes, calificaciones):
  """
  Función para mostrar una tabla con los nombres y calificaciones de los estudiantes.

  Parámetros:
    estudiantes: Una lista con los nombres de los estudiantes.
    calificaciones: Una lista con las calificaciones de los estudiantes.
  """
  print("-" * 30)
  print("| Nombre          | Calificación |")
  print("-" * 30)
  for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    calificacion = calificaciones[i]
    print(f"| {nombre:<15} | {calificacion:>10} |")
  print("-" * 30)

# Programa principal
estudiantes = []  # Lista para almacenar nombres de estudiantes
calificaciones = []  # Lista para almacenar calificaciones

cantidad_estudiantes = int(input("¿Cuántos estudiantes hay en la clase? "))

# Ingresar datos de los estudiantes
for i in range(cantidad_estudiantes):
  nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
  calificacion = float(input(f"Ingrese la calificación de {nombre}: "))

  # Almacenar datos en las listas
  estudiantes.append(nombre)
  calificaciones.append(calificacion)

# Calcular promedio general
promedio_general = calcular_promedio(calificaciones)

# Mostrar tabla de resultados
mostrar_tabla_resultados(estudiantes, calificaciones)

# Mostrar promedio general
print(f"Promedio general de la clase: {promedio_general:.2f}")
```
