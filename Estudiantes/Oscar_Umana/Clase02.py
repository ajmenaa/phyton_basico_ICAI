#operador == igualdad
x = 5
y = 5
print(x == y)

# Operador diferente !=
x = 5
y = 6
print(x != y)
#Operador menor que <
x = 5
y = 10
print(x < y)
#Operador menor o igual que <=
x = 5
y = 10
print(x <= y)
#Operador mayor >
x = 5
y = 10
print(x > y)

#Operador mayor igual que 
x = 5
y = 10
print(x >= y)

#Condiciones if
edad = int(input("cual es tu edad"))
if edad >=18 and edad <=64:
    print("Eres adulto")
elif edad >=65:
    print("eres adulto y adulto mayor")
else:
    print("eres menor de edad")
#ciclo
contador = 0
while contador <=10:
    print(contador)
    contador += 1
else:
    print("contador ya no es menor de 10")

#diccionario
usuario = {
    "nombre":"Oscar",
    "email":"oumana",
    "edad":"44",
    "peso":"90"
    }

for key in usuario:
    valor = usuario[key]
    print(valor)
    
#definir funciones
def saludar():
    mensaje = "Hola a todos"
    return mensaje
print(saludar())

def saludar2():
    mensaje = "Hola a todos"
    return mensaje
    persona = input("como te llamas")
    saludo = saludar2(persona)

print(saludar2())

