import json

archivo = open("clinica.json", "r")
#archivo = open("C:\Users\salazaor\Documents\GitHub\phyton_basico_ICAI\Estudiantes\Orlando_Salazar\ProyectoCorto\clinica.json", "r")
contenido = archivo.read()

archivo.close()

datos = json.loads(contenido)

#print(datos)

encabezados = ['Identificacion','Telefono','Provincia','Canton','Enfermedad','Medicamento']

lista_diccionarios = []

datos_diccionario = {}

for lineas in range(len(datos)):
    for encabezado in range(len(encabezados)):
        datos_diccionario[encabezados[encabezado]] = datos[lineas][encabezado]
        lista_diccionarios.append(datos_diccionario)

print(lista_diccionarios)



        
        
        
