
## 1.	Dado los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.

print('Programa para cálcular el área de un triángulo:     ') 
Base = int(input('Cuál es la Base del triángulo:    '))
Altura = int(input('Cuál es la Altura del triangulo:    '))

Área = Base * Altura /2

print(f"El area es:  {Área}")



## 2.	Convertir la cantidad de dólares ingresados por un usuario a colones y mostrar el resultado en pantalla. 

print('Convertidor de dólares a colones:     ') 
Dólares = int(input('Cuantos dólares hay:    '))
TipoCambio = int(input('Ingrese el Tipo de cambio de hoy:    '))
Colonización = Dólares / TipoCambio

print(f"Colones al día de hoy:  {Colonización}")

input('Import-Module PSReadLine')


## 3.	Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles). 

print('Promedio del Alumno: Jonathan Matamoros     ') 
Español = int(input('Nota de Español:    '))
Matemáticas = int(input('Nota de Matematicas:    '))
Economía = int(input('Nota de Economía:    '))
Programación = int(input('Nota de Programación:    '))
Ingles = int(input('Nota de Ingles:    '))

Sumadenotas = Español + Matemáticas + Economía + Programación + Ingles

Promedio = Sumadenotas / 5

print(f"El promedio de Jonathan Matamoros es:  {Promedio}")

input('Import-Module PSReadLine')