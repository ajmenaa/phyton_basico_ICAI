#Clase
class CalculadoraBasica:

    def __init__(self):
        self.Clase = 'Calculadora Básica'
        print('Bienvenido a un objeto clase ' + self.Clase)
        
    def Sumar(self):
        print('Hacer suma')
        self.Sumando1 = float(input('Ingrese el sumando 1: '))
        self.Sumando2 = float(input('Ingrese el sumando 2: '))
        self.Suma = self.Sumando1 + self.Sumando2
        print('La suma de ' + str(self.Sumando1) + ' + ' + str(self.Sumando2) + ' = ' + str(self.Suma))

    def Restar(self):
        print('Hacer resta')
        self.Minuendo = float(input('Ingrese el minuendo: '))
        self.Sustraendo = float(input('Ingrese el sustraendo: '))
        self.Diferencia = self.Minuendo - self.Sustraendo
        print('La resta de ' + str(self.Minuendo) + ' - ' + str(self.Sustraendo) + ' = ' + str(self.Diferencia))

    def Multiplicar(self):
        print('Hacer multiplicación')
        self.Factor1 = float(input('Ingrese el factor 1: '))
        self.Factor2 = float(input('Ingrese el factor 2: '))
        self.Producto = self.Factor1 * self.Factor2
        print('La multiplicación de ' + str(self.Factor1) + ' * ' + str(self.Factor2) + ' = ' + str(self.Producto))

    def Dividir(self):
        print('Hacer división')
        self.Dividendo = float(input('Ingrese el dividendo: '))
        self.Divisor = float(input('Ingrese el divisor: '))
        self.Cociente = self.Dividendo / self.Divisor
        print('La división de ' + str(self.Dividendo) + ' / ' + str(self.Divisor) + ' = ' + str(self.Cociente))

#Programa
print()
Calcu = CalculadoraBasica()
Calcu.Sumar()
print()
Calcu.Restar()
print()
Calcu.Multiplicar()
print()
Calcu.Dividir()
print()
