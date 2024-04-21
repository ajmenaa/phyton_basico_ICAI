import json
import ast

#Abre archivo JSON, lee su contenido y carga los datos parseados en la variable datos 
archivo = open("clinica.json", "r")
contenido = archivo.read()
archivo.close()
datos = json.loads(contenido)

#print(datos)
#Lista de encabezados para armar los diccionarios
encabezados = ['Identificacion','Telefono','Provincia','Canton','Enfermedad','Medicamento']

#Crea una lista de diccionarios vacia y los datos del diccionario vacios.
lista_diccionarios = []
datos_diccionario = {}

#Recorre cada linea del archivo JSON y cada item de los encabezados y va cargando la lista de diccionarios
for lineas in range(len(datos)):
    #print(lineas)
    for encabezado in range(len(encabezados)):
        #print(encabezado)
        datos_diccionario[encabezados[encabezado]] = datos[lineas][encabezado]
        paciente = str(datos_diccionario)
    #print(paciente)
    #print(datos_diccionario)
    lista_diccionarios.append(paciente)

#print(lista_diccionarios)

#Recoge todas las enfermedades y carga la lista de enfermedades
lista_enfermedades = []

for enfermedad in range(len(lista_diccionarios)):
    #print(registro)
    enfermedad_str = lista_diccionarios[enfermedad]
    #print(test_string)
    res = ast.literal_eval(enfermedad_str)
    #print(str(res))
    #print(type(res))
    enfermedades = res['Enfermedad']
    #print(enfermedades)
    #print(type(enfermedades))
    lista_enfermedades.append(enfermedades)
#print(lista_enfermedades)

#Carga unicamente la lista de enfermedades unicas descartando las que se repiten
lista_enfermedades_unicas = []

for item in lista_enfermedades:
    if item not in lista_enfermedades_unicas:
        lista_enfermedades_unicas.append(item)
        
for item in lista_enfermedades_unicas:
    print(item)
    
#Pacientes x enfermedad

        






        
        
        
