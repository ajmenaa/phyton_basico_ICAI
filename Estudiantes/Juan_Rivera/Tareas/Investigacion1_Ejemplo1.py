def Decorador(Funcion_Original):
    def Modificacion(*args, **kwargs):
        print('Instrucción adicional 1')
        Resultado = Funcion_Original(*args, **kwargs)
        print('Instrucción adicional 2')
        return Resultado
    return Modificacion

@Decorador
def Sumar(a, b):
    c = a + b
    print('Suma: ' + str(c))
    return c

Sumar(15, 30)

@Decorador
def Multiplicar(a, b, c):
    d = a * b * c
    print('Multiplicación: ' + str(d))
    return d

Multiplicar(1, 2, 3)
