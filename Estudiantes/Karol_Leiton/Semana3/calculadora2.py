
class calculadoraBasica:
    def __init__(self, num1=0, num2=0):
        self.numero1 = num1
        self.numero2 = num2

    def set_numeros(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def get_numero1(self):
        return self.numero1

    def get_numero2(self):
        return self.numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 == 0:
            return "Error: No se puede dividir por cero"
        else:
            return self.numero1 / self.numero2
        
        
        # Crear una instancia de la calculadora
mi_calculadora = calculadoraBasica()

# Pedir al usuario que ingrese dos números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

# Configurar los números en la calculadora
mi_calculadora.set_numeros(n1, n2)

# Realizar operaciones 
print("Suma:",n1," + ",n2, "= ",mi_calculadora.sumar())
print("Resta:",n1," +- ",n2, "= ", mi_calculadora.restar())
print("Multiplicación:",n1," * ",n2, "= ",mi_calculadora.multiplicar())
print("División:",n1," / ",n2, "= ",mi_calculadora.dividir())