#Ejercicio de prueba
#Stopwatch Algorithm - www.101computing.net/from-flowcharts-to-python-code/

number = float(input("Ingrese el tiempo: "))
hours = number//3600
remainder = number % 3600
minutes = remainder // 60
seconds = remainder % 60

print(f"{number} seconds = {hours} hours {minutes} minutes {seconds} seconds")

#...
