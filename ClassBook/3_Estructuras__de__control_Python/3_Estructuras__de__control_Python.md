# Booleanos, Condiciones, Bucles, Operadores Lógicos y Relacionales

## Introducción
Este notebook presenta una introducción a los conceptos básicos de programación en Python, incluyendo:

- **Valores Booleanos: True (1)** y False (0) representan valores lógicos.
- **Operadores Lógicos:** Combinan expresiones booleanas (and, or, not).
- **Condiciones:** Ejecutan bloques de código en base a condiciones booleanas (if, elif, else).
- **Bucles while:** Repiten un bloque de código hasta que una condición sea False.
- **Bucles for:** Recorren elementos de una colección (cadenas, listas, tuplas, diccionarios).

## Valores Booleanos


```python
activo = False
print('Valor:',activo,'Tipo:', type(activo)) #Imprime valor y tipo
```

    Valor: False Tipo: <class 'bool'>
    

## Operadores Relacionales


```python
numero_uno = 10
numero_dos = 20

resultado = numero_uno != numero_dos
print(resultado)
print(type(resultado))
```

    True
    <class 'bool'>
    

* Se definen dos variables numero_uno y numero_dos.
* Se utiliza el operador relacional != (diferente) para comparar los valores.
resultado almacena el resultado de la comparación (True en este caso).
* Se muestra el valor y tipo de resultado: True y bool, respectivamente.

|Operador|Resultado Booleano|
|:----|:----|
|>|Mayor|
|<|Menor|
|>=|Mayor o igual|
|<=|Menor o igual|
|==|Igual|
|!=|Diferente|


## Operadores Lógicos


```python
# AND
numero_uno = 10
numero_dos = 20
resultado = numero_uno > numero_dos and False
print(resultado)

# OR
resultado = False or False or True
print(resultado)

# NOT
numero_dos = 20
resultado = not True
resultado = not (numero_dos > 50)
print(resultado)
```

    False
    True
    True
    

- **AND (y)**: Devuelve True solo si ambas expresiones son True.
numero_uno > numero_dos es False, por lo que el resultado final es False.
- **OR (o)**: Devuelve True si al menos una expresión es True.
Todas las expresiones son False excepto la última, por lo que el resultado final es True.
- **NOT (no)**: Invierte el valor de la expresión.
not True es False.
not (numero_dos > 50) es True porque la expresión original (numero_dos > 50) es False.

## Condiciones


```python
# Condición simple
if True: #Valor Booleano
    print('Eres mayor edad')
6
# Condición con variable
edad = 15
if edad >= 18:
    print('Eres mayor edad')

# Condición con input (entrada de usuario)
edad = input("Ingresa tu edad: ") #Input retorna un String por defecto
print(type(edad))
edad = float(edad) #Conversión de String a Float
print(type(edad))

if edad >= 18:
    print('Eres mayor edad')

# Condición anidada (elif, else)
edad = int(input('Ingresa tu edad: '))
if edad >= 18 and edad <=59:
    print('Eres mayor edad')
elif edad >= 60:
     print('Eres mayor edad y eres una persona adulta')
else: #Bloque opcional
    print('No eres mayor de edad')
```

    Eres mayor edad
    <class 'str'>
    <class 'float'>
    Eres mayor edad
    Eres mayor edad
    

- Las condiciones utilizan la palabra clave if seguida de una expresión booleana.
- El bloque de código indentado con 4 espacios se ejecuta si la condición es True.
- elif permite evaluar otras condiciones si la primera falla.

## Ciclos while


```python
contador = 0
while contador <= 10:
    print(contador)
    contador +=1 #contador = contador + 1
else: #Opcional
    print ('Contador no menor o igual a 10')
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    Contador no menor o igual a 10
    

- El ciclo while repite un bloque de código hasta que la condición sea False.
- Se inicializa un contador en 0.
- El ciclo imprime el valor de contador y lo incrementa en 1.
- La condición contador <= 10 se evalúa antes de cada iteración.
- Cuando contador supera 10, el ciclo termina y se ejecuta el bloque else (opcional).

Ciclos for




```python
# Recorriendo una cadena
mensaje = "un string es un objeto inmutable" # No cambia durante la ejecución

for caracter in mensaje: #Interar sobre string
    print(caracter)

# Recorriendo una lista
numeros = [1,'Andrés',3.10,False,5]

for x in numeros:
    print(x)

# Recorriendo un diccionario (claves)
usuario = {
    'nombre':'Andrés',
    'email':'ajmena92@gmail.com',
    'pass':'password'
    }

for key in usuario:
    print(key)

# Recorriendo un diccionario (valores)
usuario = {
    'nombre':'Andrés',
    'email':'ajmena92@gmail.com',
    'pass':'password'
    }
for key in usuario: #Interar con cada elemento por medio de llave para obtener el valor
    valor = usuario[key]
    print(valor)

# Desempaquetado de clave y valor
nombre, email = ('Andrés','ajmena92@gmail.com')

usuario = {
    'nombre':'Andrés',
    'email':'ajmena92@gmail.com',
    'pass':'password'
    }
for llave,valor in usuario.items(): # Desempaquetado de la clave y el valor
    print(llave,' - ',valor)
```

    u
    n
     
    s
    t
    r
    i
    n
    g
     
    e
    s
     
    u
    n
     
    o
    b
    j
    e
    t
    o
     
    i
    n
    m
    u
    t
    a
    b
    l
    e
    1
    Andrés
    3.1
    False
    5
    nombre
    email
    pass
    Andrés
    ajmena92@gmail.com
    password
    nombre  -  Andrés
    email  -  ajmena92@gmail.com
    pass  -  password
    

- Los ciclos for recorren colecciones de elementos.
- Cadenas: Se itera sobre cada carácter del string.
- Listas: Se itera sobre cada elemento de la lista.
- Diccionarios:
 - Se itera sobre las claves del diccionario.
 - Se puede usar el desempaquetado para obtener tanto la clave como el valor.

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

    Área: 15 cm
    Perímetro: 16 cm
    Área (en metros): 70 m
    Perímetro (en metros): 34 m
    

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
while contador < 5:
  frase = input('Ingrese la frase: ')
  #contar_vocales
  cantidad_vocales = contar_vocales(frase,True)
  print(f'La frase {frase} contiene {cantidad_vocales} vocales')
  contador += 1
```

    La frase 56 contiene 0 vocales
    La frase 56 contiene 0 vocales
    La frase 56 contiene 0 vocales
    La frase 56 contiene 0 vocales
    La frase 56 contiene 0 vocales
    

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


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[11], line 43
         41 for i in range(cantidad_estudiantes):
         42   nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    ---> 43   calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
         45   # Almacenar datos en las listas
         46   estudiantes.append(nombre)
    

    ValueError: could not convert string to float: ''

