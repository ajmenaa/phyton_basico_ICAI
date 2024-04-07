""" 
1. Dado los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el
área de un triángulo. 
"""

base = input("Favor ingresar dato de base del triángulo: ")
altura = input("Favor indicar valor de la altura: ")
area_triangulo = int(base) * int(altura)

print("El área del triángulo es de:", area_triangulo)


"""  
2. Convertir la cantidad de dólares ingresados por un usuario a colones y mostrar el resultado 
en pantalla. 
"""

cantidad_dolar = input("¿Cuantos dólares desea cambiar?  ") 
tipo_cambio = input("¿Cual es el tipo de cambio? ")
colones = int(cantidad_dolar) * int(tipo_cambio)

print("El equivalente en colones es de ", colones)


""" 
3. Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar 
el resultado en pantalla. 
"""

grados_centigrados = input("¿Cual es la temperatura en grados centígrados? ")
constante_fahrenheit = 1.8
grados_fahrenheit = ((int(grados_centigrados)*constante_fahrenheit)+32)

print("El equivalente en grados Fahrenheit es de ",grados_fahrenheit)


"""  
4. Mostrar en pantalla la cantidad de segundos que tiene un lustro.
"""

años_lustro = 5
dias_año = 365
segundos_día = 86400
segundos_lustro = años_lustro * dias_año * segundos_día

print("Un lustro, es decir, 5 años, contienen un total de : ", segundos_lustro, " segundos.")


""" 
5. Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el 
resultado en pantalla. 
"""

velocidad_luz_segundo = 299792458
distancia_sol_marte = 228000000000
segundos_sol_marte = distancia_sol_marte / velocidad_luz_segundo

print("La luz del sol tarda ", segundos_sol_marte, " segundos en llegar a Marte, es decir, unos 12.67 minutos")


""" 
6. Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta 
es de 50 cm, mostrar el resultado en pantalla. 
"""

perimetro_llanta = 50 * 3.14159265358979323846
vueltas = 100000 / perimetro_llanta