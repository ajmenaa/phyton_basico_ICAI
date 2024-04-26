import json

# Nombre del archivo JSON
#nombre_archivo = "clinica.json"
#nombre_archivo ="C:/Users/ESCINF/Downloads/Proyecto I/clinica.json"

nombre_archivo = "clinica.json"
#nombre_archivo = "C:/Users/ESCINF/Downloads/Proyecto I/clinica.json"
try:
    # Abrir el archivo JSON y cargar los datos en una estructura de datos adecuada
    with open(nombre_archivo, 'r') as archivo:
        datos_clinica = json.load(archivo)
    
    # Mostrar los datos de la estructura creada
    print("Datos de la clínica:")
    for registro in datos_clinica:
        id_paciente, num_identificacion, provincia, canton, enfermedad, tratamiento = registro
        print("ID Paciente:", id_paciente)
        print("Número de Identificación:", num_identificacion)
        print("Provincia:", provincia)
        print("Canton:", canton)
        print("enfermedad:", enfermedad)
        print("Tratamiento:", tratamiento)
        print("-------------")
        

 ##-------------------------------------------------------------------------------------- 

    print ("\n\n---------------------Reporte por enfermedad especifica------------------------ ")
    aux= input("Digite la enfermedad a consultar: ")
    con=0;
    for registro in datos_clinica:
        id_paciente, num_identificacion, provincia, canton, enfermedad, tratamiento = registro
        if(enfermedad==aux):
            con=con+1
    
    print ("Cantidad de pacientes con ", enfermedad, ": ", con)
 ##-------------------------------------------------------------------------------------- 

    print ("\n\n----------------Reporte por medicamento especifico----------------- ")
    aux= input("Digite el medicamento a consultar: ")
    con=0;
    for registro in datos_clinica:
       id_paciente, num_identificacion, provincia, canton, enfermedad, tratamiento = registro
       if(tratamiento==aux):
           con=con+1
    print ("Cantidad de pacientes con ", tratamiento, " son: ", con) 
    #------------------------------------------------------------------------------------ 
    print ("\n\n-------------Comparacion de pacientes----------------- ")
    aux1= str(input("Digite el id del primer paciente: "))
    aux2= str(input("Digite el id del segundo paciente: "))
    
    enferAux="Sin enfermedad"
 
    ban=False
    
    for registro in datos_clinica:
        id_paciente1, num_identificacion1, provincia1, canton1, enfermedad1, tratamiento1 = registro

        if str(num_identificacion1)==str(aux1):
            enferAux=enfermedad1;
            for registro in datos_clinica:
                id_paciente2, num_identificacion2, provincia2, canton2, enfermedad2, tratamiento2 = registro
                if str(num_identificacion2)==str(aux2)  and  str(enfermedad2)==str(enferAux):
                    print ("Enfermedad comun: ", enfermedad2)
                    ban=True

    

    if ban==False:   
        print ("Los pacientes NO tienen enfermedades en comun");
#--------------------------------------------------------------------------------------------------
    print ("\n\n-------------Comparacion de Tratamientos----------------- ")
    aux1= str(input("Digite el id del primer paciente: "))
    aux2= str(input("Digite el id del segundo paciente: "))
    
    trataAux="Sin tratamiento"
 
    ban=False
    
    for registro in datos_clinica:
        id_paciente1, num_identificacion1, provincia1, canton1, enfermedad1, tratamiento1 = registro

        if str(num_identificacion1)==str(aux1):
            trataAux=tratamiento1;
            for registro in datos_clinica:
                id_paciente2, num_identificacion2, provincia2, canton2, enfermedad2, tratamiento2 = registro
                if str(num_identificacion2)==str(aux2)  and  str(tratamiento2)==str(trataAux):
                    print ("Tratamiento comun: ", tratamiento2)
                    ban=True

    

    if ban==False:   
        print ("Los pacientes NO tienen tratamientos en comun");
        1
#-----------------------------------------------------------------------------------------------
except FileNotFoundError:
    print(f"No se encontró el archivo {nombre_archivo}. Por favor, asegúrate de que el archivo existe en el directorio correcto.")
except json.JSONDecodeError:
    print(f"El archivo {nombre_archivo} no contiene datos JSON válidos.")
except Exception as e:
    print(f"Se produjo un error: {e}")