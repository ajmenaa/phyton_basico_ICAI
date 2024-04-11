""" DocStrings
        Esto es un comentario de multiples líneas
        Código: estos son los ejemplos vistos en la calse 1.
        Autor: Juan Carlos Rivera E.
"""

linea2 = '\n Programa Clase 1'  # \n caracter especial que representa un cambio de línea
print('Bienvenidos al curso de Python' + linea2) # Esto es un mensaje de bienvenida

print('Hola', linea2)

#Asignación de tipos de variables
mensaje = 'Hola mundo desde python'
numero = 2024
version = 2.1   #Variable tipo float
visible = False

mensaje, numero, version, visible = 'Hola G1 Python', 30, 3.1, True

print(mensaje, numero, version, visible)
print(type(mensaje))
print(type(numero))
print(type(version))
print(type(visible))

mensaje = 20
print(mensaje)
print(type(mensaje))

#leer datos -> input
nombre = input('¿Cuál es su nombre? ')
edad = input('Ingrese su edad: ')
print(f"Bienvenido: {nombre}, su edad es {edad}")
print("Bienvenido:", nombre, ", su edad es", edad)

#suma
suma = 5 + 3
print(f"La suma es: {suma}")

#resta
resta = 10 - 5
print(f"la resta es: {resta}")

#multiplicación
multiplicacion = 10 * 5
print(f"la multiplicación es: {multiplicacion}")

#División
division = 10 / 3
print(f"la división es: {division}")

#División Entera
division_entera = 10 // 3
print(f"la división entera es: {division_entera}")

#División Módulo
modulo = 33 % 2
print(f"El módulo es: {modulo}")
