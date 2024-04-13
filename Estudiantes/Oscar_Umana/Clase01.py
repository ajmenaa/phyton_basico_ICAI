print("Hola a todos al curso de Python\n") # esto es para mostrar en la consola
linea2 = ("Clase 1") # definir una variable
print("Clase de hoy\n" + linea2)
"""
esto es un comentario doc strings
de multiple linea
"""
#Asigancion de variables#python reconoce el tipo de variable
var1 = "primer valor"
var2 = 15
var3 = 2,1
var4 = False
print("los valores son:", var1, var2, var3, var4)
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
#Asignacion de tupla
var1, var2, var3, var4 = "hola", 100, 5.7, True
print("los valores son:", var1, var2, var3, var4)
#Leer datos del usuario
nombre = input("ingresa tu nombre:")
edad = input("ingresa tu edad:")
print("Bienvenido", nombre, "tu edad es", edad)
#con formato
print(f"Bienvenido:"{nombre},"Tu edad es:"{edad})