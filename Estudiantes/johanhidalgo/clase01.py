print('Bienvenidos a Python Basico')
linea2 = '\n programa de la clase 1'
print('Grupo1' + linea2)

"""" Docs Strings
Esto es un comentario de multiples lineas 
Código estos son los ejemplos visto en la clase 1
Autor: Johan Hidalgo
"""
linea2='\n Programa Clase 1' # Esto es un caracter especial 
print('Bienvenidos al curso de Python'+ linea2)

print('Hola', linea2)

# Trabajar con diferentes tipos de datos en Python
#Tipado dinamico: El define que tipo de dato, decimal es flotante
# Tres reglas para asignar variables son en minusculas, no pueden empezar con numeros y no pueden ser palabras reservadas
# Asignación de tipos de variables los espacios representan Jerarquias 

mensaje = 'Hola mundo desde python'
numero = 2024
version = 2,1 # Variable tipo float
visible = False
Visible = True
print(visible,Visible)
print(mensaje,numero,version,visible,Visible)

#Asignación en tupla
mensaje,numero,version,visible ='Hola en python', 30, 1.1, True

print(type(mensaje))
print(type(numero))
print(type(version))
print(type(visible))

#Cambio de inferencia de tipo 
mensaje = 20
print(type(mensaje))
# Mensajes deben ser cortos
#nombre_completo
#lista_compras 
#coordenadas_x

#Leer datos > input 

nombre = input('¿Cual es su nombre?')
edad = input('Ingrese su edad:')
print(f"Bienvenido:{nombre},su edad es:{edad}")
print("Bienvenido:",nombre, "su edad es:", edad)

""" Operadores
"""

#Suma
suma = 5 + 3 
print(f"La suma es: {suma}")

#Resta
resta = 5 - 3 
print(f"La resta es: {resta}")

#Multiplicación
multiplicacion = 5 * 3 
print(f"La multiplicación es: {multiplicacion}")

# Division
division = 25/5
print(f"La division es: {division}")

#División entera 
division_entera = 10//3
print(f"La division es: {division_entera}")

#División modular 
modulo = 33 % 2
print(f"El modulo es: {modulo}")



