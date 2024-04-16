archivo = open("clinica.json", "r")
contenido = archivo.read()
archivo.close()

i = 0
a = 0

for registros in contenido:
    print(contenido[i])
    i += 1