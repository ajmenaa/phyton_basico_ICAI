""" 
Titulo:            LaCalculadora.py
Descripcion:       Proyecto Calculadora basica utilizando el instanciamiento de una clase CalculadoraBasica que realiza las cuatro operaciones basicas
Requirimientos:    Interprete Python
Uso:               py .\\LaCalculadora.py 
Escrito por:       Orlando Salazar<orsaac@gmail.com>
Fecha:             2024-04-22
 """
 
class CalculadoraBasica:
    def __init__(self):
        self.n1 = float(input("Introduce tu primer numero: "))
        self.n2 = float(input("Introduce tu segundo numero: "))

    def sumar(self):
        return self.n1 + self.n2

    def restar(self):
        return self.n1 - self.n2

    def multiplicar(self):
        return self.n1 * self.n2
    
    def dividir(self):
        return self.n1 / self.n2

if __name__ == "__main__":
    mi_calculadora = CalculadoraBasica()

    print("\n¿Que operacion matematica quieres hacer?")
    print("1) Sumar los dos numeros")
    print("2) Restar los dos numeros")
    print("3) Multiplicar los dos numeros")
    print("4) Dividir el primer numero entre el segundo numero")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print(f"\nRESULTADO: La suma de {mi_calculadora.n1} + {mi_calculadora.n2} es igual a {mi_calculadora.sumar()}")
    elif opcion == 2:
        print(f"\nRESULTADO: La resta de {mi_calculadora.n1} - {mi_calculadora.n2} es igual a {mi_calculadora.restar()}")
    elif opcion == 3:
        print(f"\nRESULTADO: El producto de {mi_calculadora.n1} * {mi_calculadora.n2} es igual a {mi_calculadora.multiplicar()}")
    elif opcion == 4:
        print(f"\nRESULTADO: El resultado de dividir {mi_calculadora.n1} / {mi_calculadora.n2} es igual a {mi_calculadora.dividir()}")
    else:
        print("Opción incorrecta")
