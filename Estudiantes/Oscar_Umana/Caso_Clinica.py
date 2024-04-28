#este programa permite determinar datos de pacientes provenientes de una lista

lista_pacientes = [
["123", 89076541, "Heredia", "Barva", "gripe", "acetaminofen"],
["321", 31321321, "Cartago", "Pacayas", "gastritis", "antiacido"],
["456", 87539856, "San Jose", "Pavas", "tos", "jarabe"],
["789", 45522221, "Limón", "Puerto Viejo", "migraña", "acetaminofen"],
["345", 45354632, "Guanacaste", "Liberia", "dolor", "acetaminofen"],
["123", 89076541, "Heredia", "Barva", "migraña", "acetaminofen"],
["456", 87539856, "San Jose", "Pavas", "dolor", "acetaminofen"],
["456", 87539856, "San Jose", "Pavas", "dolor", "jarabe"],
["345", 45354632, "Guanacaste", "Liberia", "gripe", "acetaminofen"],
["789", 45522221, "Limón", "Puerto Viejo", "presion", "acetaminofen"]
]
#print(lista_pacientes)










#for elemento in lista_pacientes:
    #print(str(elemento[0][0:5]))
    
for elemento_1 in lista_pacientes:
    for datos in elemento_1:
        if datos == "gripe":
            print("tenemos un paciente que padece de:", datos)
        if datos == "tos":
            print("tenemos un paciente que padece de:", datos)            
        if datos == "antiacido": 
            print("tenemos un paciente que padece de:", datos)
        if datos == "presion":
            print("tenemos un paciente que padece de:", datos)
        if datos == "dolor":
            print("tenemos un paciente que padece de:", datos)
        if datos == "gastritis":
            print("tenemos un paciente que padece de:", datos)
        
    
for elemento_2 in lista_pacientes:
    for datos2 in elemento_2:
        
        if datos2 == "acetaminofen":            
            print("tenemos un paciente que toma:", datos2) 
        if datos2 == "jarabe":
            print("tenemos un paciente que toma:", datos2)            
        if datos2 == "antiacido": 
            print("tenemos un paciente que toma:", datos2)
        
    

        
   
   
   # if elemento_1[0:9][4]== enfermedad_1:
    #    elemento_1 += elemento_1  
     #   print("los casos de gripe son:", elemento_1)
    #else:
     #   print("No hay casos de gripe")
        
    
    
    
#for elemento in lista_pacientes:   
    #print(str(elemento[1][0:5]))
#for elemento in lista_pacientes:
    #print(str(elemento[2][0:5]))
#for elemento in lista_pacientes:
    #print(str(elemento[3][0:5]))
#for elemento in lista_pacientes:   
    #print(str(elemento[4][0:5]))
#for elemento in lista_pacientes:
    #print(str(elemento[5][0:5]))
