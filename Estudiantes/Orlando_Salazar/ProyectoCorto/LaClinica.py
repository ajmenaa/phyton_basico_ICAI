import json
import ast
from collections import Counter
import os

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
lista_enfermedades = []
lista_enfermedades_unicas = []
lista_medicamentos = []
lista_medicamentos_unicos = []

def press_any_key_to_continue():
    input()  # Wait for user input (Enter key)
    print('Presione una tecla para continuar...')


def reporte_enfermedades():
    #Lista todas las enfermedades y carga la lista de enfermedades
    print('************Reporte de enfermedades************\n')
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
    

    #Carga unicamente la lista de enfermedades unicas descartando las que se repiten
    
    for item in lista_enfermedades:
        if item not in lista_enfermedades_unicas:
            #global lista_enfermedades_unicas
            lista_enfermedades_unicas.append(item)
    print("La lista de enfermedades que se atienden en la clinica son las siguientes: \n")        
    for item in lista_enfermedades_unicas:
        print(item)
    
#Pacientes x enfermedad
#pacientes_por_enfermedad = Counter(lista_enfermedades)
#print(pacientes_por_enfermedad)
#print(pacientes_por_enfermedad['dolor'])
def pacientes_por_enfermedad():
    lista_pacientes_por_enfermedad = []
    print('************Reporte de pacientes por enfermedad************\n')
    for pacientes in range(len(lista_diccionarios)):
        datos_paciente = str(lista_diccionarios[pacientes])
        #print(datos_paciente)          
        res = ast.literal_eval(datos_paciente)
        id_paciente = res['Identificacion']
        enfermedad_paciente = res['Enfermedad']
        tupla_paciente_enfermedad = (id_paciente,enfermedad_paciente)
        #print(tupla_paciente_enfermedad)
        if tupla_paciente_enfermedad not in lista_pacientes_por_enfermedad:
            lista_pacientes_por_enfermedad.append(tupla_paciente_enfermedad)
    #print(lista_pacientes_por_enfermedad)
    for item in range(len(lista_enfermedades_unicas)):
        valor_a_contar = lista_enfermedades_unicas[item]
        #print(valor_a_contar)
        for tuplas in range(len(lista_pacientes_por_enfermedad)):
            conteo = sum(tupla.count(valor_a_contar) for tupla in lista_pacientes_por_enfermedad)
        print(f"Existen {conteo} pacientes para la enfermedad {valor_a_contar} .")
    

def reporte_medicamentos():    
#Lista todos los medicamentos recetados en la clinica
    print('************Reporte de medicamentos************\n')
    for medicamento in range(len(lista_diccionarios)):
        medicamento_str = lista_diccionarios[medicamento]
        res = ast.literal_eval(medicamento_str)
        medicamentos = res['Medicamento']
        lista_medicamentos.append(medicamentos)
    #print(lista_medicamentos)

    #Carga unicamente la lista de medicamentos unicas descartando las que se repiten
    

    for item in lista_medicamentos:
        if item not in lista_medicamentos_unicos:
            lista_medicamentos_unicos.append(item)
    print("La lista de medicamentos que se entregan en la clinica son los siguientes: \n")         
    for item in lista_medicamentos_unicos:
        print(item)
    
#Medicamentos x paciente
#medicamentos_por_paciente = Counter(lista_medicamentos)
#print(medicamentos_por_paciente)
#print(medicamentos_por_paciente['acetaminofen'])
def pacientes_por_medicamento():
    print('************Reporte de pacientes por medicamento************\n')
    lista_pacientes_por_medicamento = []
    for pacientes in range(len(lista_diccionarios)):
        datos_paciente = str(lista_diccionarios[pacientes])
        #print(datos_paciente)          
        res = ast.literal_eval(datos_paciente)
        id_paciente = res['Identificacion']
        medicamento_paciente = res['Medicamento']
        tupla_paciente_medicamento = (id_paciente,medicamento_paciente)
        #print(tupla_paciente_enfermedad)
        if tupla_paciente_medicamento not in lista_pacientes_por_medicamento:
            lista_pacientes_por_medicamento.append(tupla_paciente_medicamento)
    #print(lista_pacientes_por_enfermedad)
    for item in range(len(lista_medicamentos_unicos)):
        valor_a_contar = lista_medicamentos_unicos[item]
        #print(valor_a_contar)
        for tuplas in range(len(lista_pacientes_por_medicamento)):
            conteo = sum(tupla.count(valor_a_contar) for tupla in lista_pacientes_por_medicamento)
        print(f"Existen {conteo} pacientes para el medicamento {valor_a_contar} .")
        
def mostrar_menu():
    """
    Funcion para mostrar un menu de opciones al usuario
    """
    os.system('cls')
    print('**********************Sistema Informatico La Clinica*********************************')
    print('\n')
    print('Escoja alguna de las siguientes opciones:')
    print('\n')
    print('a. Mostrar reporte de enfermedades que se tratan en la clinica.')
    print('\n')
    print('b. Mostrar reporte de pacientes por enfermedad.')
    print('\n')
    print('c. Mostrar reporte de medicamentos recetados en la clinica.')
    print('\n')
    print('d. Mostrar reporte de pacientes por medicamento.')
    print('\n')
    print('e. Comparar pacientes.')
    print('\n')
    print('s. Salir del programa.')
    print('\n')
    
    opcion = input('Digite la opcion seleccionada: ')
    
    match opcion:
        case 'a':
            os.system('cls')
            reporte_enfermedades()
            press_any_key_to_continue()
            mostrar_menu()
        case 'b':
            os.system('cls')
            pacientes_por_enfermedad()
            press_any_key_to_continue()
            mostrar_menu()
        case 'c':
            os.system('cls')
            reporte_medicamentos()
            press_any_key_to_continue()
            mostrar_menu()
        case 'd':
            os.system('cls')
            pacientes_por_medicamento()
            press_any_key_to_continue()
            mostrar_menu()
        case 'e':
            os.system('cls')
            #compara_pacientes()
            press_any_key_to_continue()
            mostrar_menu()
        case 's':
            quit()
        case _:
            print("Opcion Invalida")
            press_any_key_to_continue()
            mostrar_menu()

mostrar_menu()

        
        
