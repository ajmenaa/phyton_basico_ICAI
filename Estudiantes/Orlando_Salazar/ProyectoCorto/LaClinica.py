import json

archivo = open("clinica.json", "r")
contenido = archivo.read()

archivo.close()

datos = json.loads(contenido)

print(datos[0][5])


        
        
        
