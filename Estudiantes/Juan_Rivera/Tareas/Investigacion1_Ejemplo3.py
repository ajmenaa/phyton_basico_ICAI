def Funcion(a, b, c):
    print('Variable a: ' + str(a))
    yield a
    print('Variable b: ' + str(b))
    yield a + b
    print('Variable c: ' + str(c))
    a + b + c
    yield a + b + c

Resultado = Funcion(1, 2, 3)
print('Resultado: ' + str(next(Resultado)))
print('Resultado: ' + str(next(Resultado)))
print('Resultado: ' + str(next(Resultado)))
