import numpy as np

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

a1 = np.array(lista_pacientes)
print(a1)
print(a1[a1=="gripe"])
gripe = np.array(a1[a1=="gripe"])
print("La cantidad de pacientes atendidos con gripe es de", gripe.size)
tos = np.array(a1[a1=="tos"])
print("La cantidad de pacientes atendidos con tos es de", tos.size)
gastri = np.array(a1[a1=="gastritis"])
print("La cantidad de pacientes atendidos por gastritis es de", gastri.size)
dolor = np.array(a1[a1=="dolor"])
print("La cantidad de pacientes atendidos por dolor es de", dolor.size)
migra = np.array(a1[a1=="migraña"])
print("La cantidad de pacientes atendidos por migraña es de", migra.size)
presion = np.array(a1[a1=="presion"])
print("La cantidad de pacientes atendidos por presion es de", presion.size)
# reporte de Medicamentos
med_1 = np.array(a1[a1=="acetaminofen"])
med_2 = np.array(a1[a1=="jarabe"])
med_3 = np.array(a1[a1=="antiacido"]) 
med_t = med_1.size + med_2.size + med_3.size
print("La cantidad de medicamentos recetados a los pacientes es de:", med_t)

print("La cantidad de pacientes que toman acetaminofen es de:", med_1.size)
print("La cantidad de pacientes que toman jarabe es de:", med_2.size)
print("La cantidad de pacientes que toman antiacido es de:", med_3.size)

Id_paciente_1 = input("ingrese un numero de pacientes, entre estas opciones: 123, 456, 789 y 345:") 
Id_paciente_2 = input("ingrese un segundo numero de pacientes, entre estas opciones: 123, 456, 789 y 345:")


