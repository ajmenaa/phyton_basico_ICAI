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