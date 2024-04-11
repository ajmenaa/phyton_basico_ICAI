
# ¿Que es Python?

Bueno, ¿sabes qué? Python es un lenguaje de programación absolutamente
increíble. Fue creado por Guido van Rossum en 1991, y desde entonces ha
sido adoptado por algunas de las empresas más innovadoras y exitosas del
mundo, como Google, Facebook y Dropbox.

1.  Es un lenguaje de programación interpretado de alto nivel. Esto
    significa que el código de Python no necesita ser compilado antes de
    ser ejecutado, como sucede en otros lenguajes de programación.
2.  Fue creado en 1991 por Guido van Rossum en los Países Bajos. El
    nombre de Python fue inspirado en el grupo de comediantes británicos
    Monty Python.
3.  Es un lenguaje de programación multiplataforma, lo que significa que
    se puede ejecutar en diferentes sistemas operativos como Windows,
    Linux y macOS.
4.  Python es un lenguaje de programación de propósito general, lo que
    significa que se puede utilizar para crear una amplia variedad de
    programas y aplicaciones, como aplicaciones de escritorio,
    aplicaciones web, herramientas de automatización, aplicaciones
    científicas y de análisis de datos, entre otras.
5.  Python es un lenguaje de programación de código abierto y tiene una
    gran comunidad de desarrolladores en todo el mundo. Esto significa
    que hay una gran cantidad de recursos en línea, bibliotecas y
    módulos disponibles para Python.
6.  Python es conocido por su sintaxis clara y legible, lo que lo hace
    fácil de aprender para principiantes. La filosofía de diseño de
    Python se enfoca en la legibilidad del código, lo que significa que
    el código debe ser fácil de entender y leer para los humanos.
7.  Una de las mayores fortalezas de Python es su amplia colección de
    bibliotecas y módulos, que permiten a los programadores realizar
    tareas complejas con muy pocas líneas de código.
8.  Python también es utilizado ampliamente en áreas como la ciencia de
    datos, la inteligencia artificial, el aprendizaje automático, y la
    automatización de tareas, gracias a bibliotecas especializadas como
    NumPy, Pandas, TensorFlow y Selenium, entre otras.

El código fuente es el conjunto de instrucciones escritas en un lenguaje
de programación específico que un programador escribe para crear un
programa de software. El código fuente es el texto que se puede leer y
editar con un editor de texto simple. Este código es lo que el
compilador o intérprete utiliza para convertir el programa en un formato
que la computadora pueda entender y ejecutar. Por otro lado, un IDE
(Integrated Development Environment) o Entorno de Desarrollo Integrado
en español, es un software que proporciona herramientas y funciones para
facilitar el desarrollo de software. Un IDE típicamente incluye un
editor de código, un depurador, un compilador o intérprete, herramientas
para refactorizar código, y otras características útiles para
desarrollar software.
:::


# Sintaxis y Comentarios

-   Comentarios de linea, multiple linea
-   Sintaxis identada
-   Salidas -\> print()

``` python
""" Docstrings
    Esto es un comentario de multiples lineas
    Codigo: vistos en la primera clase de Python
    Autor: Andrés Mena Abarca
"""
print('Bienvenidos a Python Basico') # Esto es un comentario de linea

#··
linea2 = "\n Programa Clase 1" #\n caracter especial que representa un salto de línea
print('Bienvenidos a Python Basico' + linea2)

#...
print('Bienvenidos a Python Basico',linea2)
```
-   Comillas dobles: Se utilizan para la interpolación de variables y
    para cadenas de texto que abarcan varias líneas.
-   Comillas simples: Se utilizan para cadenas de texto simples que no
    requieren interpolación de variables.
------------------------------------------------------------------------

# Trabajemos con los diferentes tipos de datos en Python

-   String: Cadenas de caracteres -\>\"string\" -\>\'string\'
-   Enteros
-   Flotantes -\> Decimal
-   Boleanos \# True -\>1 False -\>0

### **La inferencia de tipos en Python:**

La inferencia de tipos es una característica de Python que permite al
intérprete deducir el tipo de dato de una variable a partir del contexto
en el que se usa.

### **Sintaxis Variables:**

1.  Empezar con una letra o guion bajo (\_).
2.  Contener solo letras, números y guiones bajos.
3.  No ser palabras clave reservadas del lenguaje Python.


``` python
#Asignación individual
mensaje = "Hola mundo desde Python:"
numero = 2023
version = 2.1 #Variable que Gestiona la versión del Sistema
visible = False

#Asignación de tupla
mensaje, numero, version, visible = "Hola Mundo", 'desde Python', 3.1, True

print(mensaje, numero, version,visible)
print(type(mensaje))
print(type(numero))
print(type(version))
print(type(visible))
```

## **Consejos para elegir nombres de variables correctos:**

-   Ser descriptivos: Deben indicar el contenido de la variable.
-   Ser cortos y simples: Deben ser fáciles de recordar y escribir.
-   Ser consistentes: Usar el mismo estilo de mayúsculas y minúsculas.
-   Evitar palabras clave: No usar palabras reservadas del lenguaje
    Python.
-   Utilizar prefijos y sufijos: Se pueden usar para agrupar variables
    relacionadas.

**Ejemplo de nombres de variables correctos:**

-   nombre_completo: Almacena el nombre completo de una persona.
-   edad: Almacena la edad de una persona.
-   lista_de_compras: Almacena una lista de productos para comprar.
-   oordenada_x: Almacena la coordenada X de un punto.


### Leer Datos -\> input

``` python
nombre = input("¿Cual es su nombre? ")
edad = input("Ingrese su edad: ")
print('Bienvenido:',nombre,edad,"años")
print(type(edad)) #Si bien leo un numero entero, capturo un string
```

### Operadores aritméticos:

-   Suma: +
-   Resta: -
-   Multiplicación: \*
-   División: /
-   División entera: //
-   Módulo (residuo de la división) %


``` python
# Suma
suma = 10 + 5
print(f"La suma es: {suma}") #Se pueden utilizar f-strings para formatear cadenas de texto de forma más flexible

# Resta
resta = 10 - 5
print(f"La resta es: {resta}")

# Multiplicación
multiplicacion = 10 * 5
print(f"La multiplicación es: {multiplicacion}")

# División
division = 10 / 5
print(f"La división es: {division}")

# División entera
division_entera = 10 // 5
print(f"La división entera es: {division_entera}")

# Módulo
modulo = 10 % 5
print(f"El módulo es: {modulo}")
```

### Ejemplo simple de cómo leer y mostrar data

``` python
# Se solicitan al usuario la base y la altura del triángulo.
base = int(input("Ingrese el valor de la base, por favor: "))
altura = int(input("Ingrese el valor de la altura, por favor: "))

# Se muestran los tipos de dato de las variables.
print(type(base))
print(type(altura))

# Se calcula el área del triángulo.
area = (base * altura) / 2

# Se muestra el resultado del área del triángulo al usuario.
print(f"El área del triángulo es: {area}")

# Se espera que el usuario presione una tecla para salir.
input("Presione una tecla para salir...")
```

------------------------------------------------------------------------

## Manejo de Cadenas de Texto en Python

En Python, las cadenas de texto (strings) son objetos inmutables que se
pueden manipular de diversas maneras. Las operaciones que se pueden
realizar sobre las cadenas de texto incluyen:

1. **Concatenación:** Se utiliza el operador + para unir dos cadenas de
    texto.


``` python
cadena1 = "Hola"
cadena2 = "mundo!"

cadena_concatenada = cadena1 + " " + cadena2

print(cadena_concatenada)
```


2. **Repetición:** Se utiliza el operador \* para repetir una cadena de
    texto un número determinado de veces.


``` python
cadena = "Hola"

cadena_repetida = cadena * 5

print(cadena_repetida)
```

3. **Indexación y corte:**

-   Se pueden acceder a los caracteres de una cadena de texto utilizando
    índices.
-   Se pueden obtener subcadenas de una cadena de texto utilizando el
    operador de corte (\[:\]).
``` python
cadena = "Hola Python!"

# Acceder a un caracter
print(cadena[0])

# Obtener una subcadena
print(cadena[6:])
```


4. **Métodos de las cadenas:** Las cadenas de texto en Python tienen una
    gran cantidad de métodos que se pueden utilizar para realizar
    diversas operaciones. Algunos de los métodos más comunes son:

-   **upper():** Convierte la cadena a mayúsculas.
-   **lower():** Convierte la cadena a minúsculas.
-   **strip():** Elimina los espacios en blanco al principio y al final
    de la cadena.
-   **find():** Busca la primera aparición de una subcadena en la
    cadena.
-   **replace():** Reemplaza una subcadena por otra en la cadena.

``` python
#MAYUSCULA
texto = "hola estudiantes"
x = texto.upper()
print(x)

#MINUSCULA
texto = "hola PROFES"
x = texto.lower()
print(x)


#CONVERTIR EN MAYUSCULA LA PRIMERA LETRA
texto = "saludos bienvenidos al curso de PYTHON"
x = texto.capitalize()
print(x)

texto = "2023 saludos bienvenidos al curso de PYTHON"
x = texto.capitalize()
print(x)

#INVERSOR
texto = "2023 saludos bienvenidos al CURSO DE PYTHON"
x = texto.swapcase()
print(x)

#REPLACE
texto = "Hola mi nombre es Andrés"
print(texto.replace("Hola","Saludos"))

ced = "1-1111-1111"
x= ced.replace("-","")
print(x)

# Comprobar si la cadena solo contiene letras
cadena = "Hola"
print(cadena.isalpha())
# True

# Comprobar si la cadena solo contiene números
cadena = "123"
print(cadena.isdigit())
# True

# Buscar la primera aparición de una subcadena
cadena = "Hola mundo!"
print(cadena.find("mundo"))
# Salida:
# 6

#CONTAR CUANTAS VECES APARECE UNA PALABRA
``` python
txt= "Este es curso Python y sera muy interactivo muy Python"
x = txt.count("Python")
print(x)
```
# Convenciones de Python (PEP 8)

Las convenciones de Python, también conocidas como PEP 8 (Python
Enhancement Proposal 8), son un conjunto de lineamientos para escribir
código Python de forma legible, consistente y mantenible. Estas
convenciones abarcan desde el estilo de nombrado de variables hasta la
estructura del código.

## 1. Nombrado: 
-   **Letras y guiones bajos:** Los nombres de variables, funciones,
    clases y módulos deben comenzar con una letra o guion bajo y pueden
    contener letras, números y guiones bajos.
-   **Mayúsculas y minúsculas:** Caso serpiente (snake_case): Se utiliza
    para variables y funciones. Las palabras se separan con guiones
    bajos. (Ej: total_costo)
-   **CamelCase:** Se utiliza para clases y nombres de archivos. La
    primera letra de cada palabra se escribe en mayúscula. (Ej:
    MiClasePrincipal)
-   **Constantes:** Se escriben en
    MAYÚSCULAS_SEPARADAS_POR_GUIONES_BAJOS. (Ej: PI, MAX_VELOCIDAD)
    Palabras reservadas: Evita usar palabras clave del lenguaje Python
    como nombres de variables.

## 2. Sangría: 
-   **Bloques de código:** La sangría (generalmente 4 espacios) se
    utiliza para definir bloques de código dentro de funciones, bucles,
    condicionales, etc. La sangría consistente es crucial para la
    legibilidad del código.

## 3. Comentarios: 

-   **Docstrings:** Se utilizan para documentar funciones, clases y
    módulos. Proporcionan información sobre su propósito, parámetros y
    valores de retorno.
-   **Comentarios en línea:** Se utilizan para explicar partes
    específicas del código y mejorar la comprensión del mismo.

## 4. Espacios en blanco: 

-   **Separadores:** Se utilizan espacios en blanco alrededor de
    operadores, después de comas, antes y después de paréntesis,
    corchetes y llaves.
-   **Líneas en blanco:** Se utilizan para separar secciones lógicas del
    código y mejorar la legibilidad.

## 5. Importaciones: {#5-importaciones}

-   **Módulos estándar:** Se importan al inicio del código utilizando la
    instrucción import.
-   **Funciones y clases de otros módulos:** Se importan utilizando la
    instrucción from `<modulo>`{=html} import `<nombre>`{=html}.

# Beneficios de usar las convenciones de Python:

-   **Legibilidad:** El código es más fácil de leer y comprender para
    otros programadores.
-   **Mantenibilidad**: El código es más fácil de modificar y
    actualizar.
-   **Colaboración:** Las convenciones facilitan el trabajo en equipo.
-   **Herramientas:** Muchas herramientas de análisis de código y
    linters se basan en las convenciones de Python para detectar
    posibles errores de estilo.

Ejemplo de código con las convenciones de Python:

``` python
def mi_funcion(param1, param2):
  """
  Esta función realiza una tarea específica.

  Parámetros:
    param1: El primer parámetro de la función.
    param2: El segundo parámetro de la función.

  Retorno:
    El resultado de la función.
  """

  # Se realiza una operación con los parámetros
  resultado = param1 + param2

  # Se retorna el resultado
  return resultado

# Se llama a la función
resultado = mi_funcion(10, 20)

# Se imprime el resultado
print(resultado)
```

# Recursos adicionales:

-   PEP 8 Style Guide for Python Code:
    <https://peps.python.org/pep-0008/>
-   Guía de estilo para el código Python -- PEP 8 en Español:
    <https://recursospython.com/pep8es.pdf>
-   El Pythonista - Guía de estilos en Python:
    <https://elpythonista.com/pep-8>

