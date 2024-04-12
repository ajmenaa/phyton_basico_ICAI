#Primer ejercicio 
base = float(input("Ingrese base: "))
altura = float(input("Ingrese altura: "))
resultado = base * altura
print(f"El área es {resultado}")

#Segundo ejercicio
monto_dolares = float(input("Ingrese monto en dolares: "))
tipo_cambio = float(input("Tipo de cambio del día: "))
resultado = monto_dolares*tipo_cambio
print(f"El monto colonizado es {resultado}")

#Tercer ejercicio
grados_centigrados = float(input("Ingreses grados centigrados: "))
resultado = (grados_centigrados* 9/5)+32
print(f"Los grados Fahrenheit {resultado}")

#Ejercicio de prueba
#Stopwatch Algorithm - www.101computing.net/from-flowcharts-to-python-code/

number = float(input("Ingrese el tiempo: "))
hours = number//3600
remainder = number % 3600
minutes = remainder // 60
seconds = remainder % 60

print(f"{number} seconds = {hours} hours {minutes} minutes {seconds} seconds")

#...