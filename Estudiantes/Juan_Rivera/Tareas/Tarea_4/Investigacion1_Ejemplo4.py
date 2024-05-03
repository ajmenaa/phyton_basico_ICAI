def Funcion(a, b, c):
    print('Variable a: ' + str(a))
    yield a
    print('Variable b: ' + str(b))
    yield a + b
    print('Variable c: ' + str(c))
    yield a + b + c

for i in Funcion(1, 2, 3):
    print('Resultado: ' + str(i))
