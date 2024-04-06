""" Este es un comentario que puede 
ocupar varias líneas, en donde se puede detallar el autor, que función cumple el código, 
su alcance, etc """

linea2 = '\n Programa Clase 1' # \n es un caracte especial que representa un salto de línea
print('Bienvenidos al curso de Python' + linea2) #Esto es un mensaje de bienvenida

print("Hola", linea2)



#Asignación tipos de variables individual
mensaje = 'Hola mundo desde python'
numero = 2024
version = 2.1 #variable tipo float o flotante
visible = False

#Asignación de tupla
mensaje,numero, version, visible = 'Hola G1 Python',30,3.1, True


print (mensaje, numero, version, visible)
print(type(mensaje))
print(type(numero))
print(type(version))
print(type(visible))

#Cambio de inferencia de tipo
mensaje = 20
print (mensaje)
print(type(mensaje))

#leer datos -> input
nombre = input('¿Cual es su nombre? ')
edad = input('Ingrese su edad: ')
print(f"Bienvenido: {nombre}, su edad es {edad}")

print("Bienvenido", nombre, "su edad es", edad)

# Operadores
suma = 5 + 3
print(f"La suma es: {suma}")

resta = 10 - 5
print(f"La resta es: {resta}")

multiplicacion = 7 * 8
print(f"La multiplicación es: {multiplicacion}")
      
division = 20 / 5
print(f"La división es: {division}")

division_entera = 10 // 3
print(f"la división entera es: {division_entera}")

division_modular = 33 % 2
print(f"el modulo es:{division_modular}")