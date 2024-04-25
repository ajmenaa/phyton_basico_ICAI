def Decorador(Funcion_Original):
    def Modificacion(*args, **kwargs):
        print('Instrucción adicional 1')
        Resultado = Funcion_Original(*args, **kwargs)
        print('Instrucción adicional 2')
        return Resultado
    return Modificacion

@Decorador
def Restar(a, b):
    c = a - b
    print('Resta: ' + str(c))
    return c

Restar(15, 30)

@Decorador
def Dividir(a, b):
    c = a / b
    print('División: ' + str(c))
    return c

Dividir(1, 2)