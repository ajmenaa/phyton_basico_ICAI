#Programa que hace operaciones básicas

def sumar(num1,num2):
    total = num1 + num2
    return total

def restar(num1, num2):
    total_restar = num1 - num2
    return total_restar

def multiplicar(num1, num2):
    total_multi = num1*num2
    return total_multi

def dividir(num1, num2):
    total_div = num1/num2
    return total_div

print("esta es una calculadora, sigue las instrucciones:")

opcion = int(input("Ingresa 1 para sumar, 2 para restar, 3 para multiplicar o 4 para dividir:  "))

num1 = int(input("Ingresa el primer numero:  "))
num2 = int(input("Ingresa el segundo numero:  , Cuidado si vas a dividr este numero no puede ser cero"))

if opcion == 1:
    print("El resultado de la suma es  ", sumar(num1,num2))
if opcion == 2:
    print("El resultado de la resta es  ", restar(num1,num2))
if opcion == 3:
    print("El resultado de la multiplicacion es  ", multiplicar(num1,num2))
if opcion == 4:
    print("El resultado de la division es  ", dividir(num1,num2))

    



