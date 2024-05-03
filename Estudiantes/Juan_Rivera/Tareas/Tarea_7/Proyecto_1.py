#Función Cargar Tabla
def CargarTabla():
    diccionario = {'Identificacion': 0, 'Telefono': 0, 'Provincia': '', 'Canton': '', 'Enfermedad': '', 'Medicamento': ''}

    archivo = open('clinica.json', 'r')

    tabla = []
    for linea in archivo:
        linea = linea.lstrip()
        linea = linea.rstrip(',')
        linea = linea.replace('[', '')
        linea = linea.replace(']', '')
        linea = linea.replace('"', '')
        linea = linea.replace(', ', ',')
    
        lista = linea.split(',')
        largo = len(lista)
        if largo > 1:
            i = 0
            for clave in diccionario:
                diccionario[clave] = lista[i]
                i = i + 1

            tabla.append(diccionario.copy())

    archivo.close()
    return tabla

#Función Generar Reporte Enfermedades
def GenerarReporteEnfermedades(tabla):
    enfermedades = {}
    PacienteEnfermedad = {}
    ListaPacienteEnfermedad = []

    for diccionario in tabla:
        PacienteEnfermedad = {'Idenfificacion: ': diccionario['Identificacion'], 'Enfermedad': diccionario['Enfermedad']}
        if PacienteEnfermedad not in(ListaPacienteEnfermedad):
            ListaPacienteEnfermedad.append(PacienteEnfermedad.copy())

    for diccionario in ListaPacienteEnfermedad:
        for clave in diccionario:
            if clave == 'Enfermedad':
                enfermedad = diccionario[clave]
                enfermedades[enfermedad] = 0

    for diccionario in ListaPacienteEnfermedad:   
        enfermedades[diccionario['Enfermedad']] = enfermedades[diccionario['Enfermedad']] + 1

    return enfermedades

#Función Generar Reporte Medicamentos
def GenerarReporteMedicamentos(tabla):
    medicamentos = {}
    PacienteMedicamento = {}
    ListaPacienteMedicamento = []

    for diccionario in tabla:
        PacienteMedicamento = {'Idenfificacion: ': diccionario['Identificacion'], 'Medicamento': diccionario['Medicamento']}
        if PacienteMedicamento not in(ListaPacienteMedicamento):
            ListaPacienteMedicamento.append(PacienteMedicamento.copy())

    for diccionario in ListaPacienteMedicamento:
        for clave in diccionario:
            if clave == 'Medicamento':
                medicamento = diccionario[clave]
                medicamentos[medicamento] = 0

    for diccionario in ListaPacienteMedicamento:   
        medicamentos[diccionario['Medicamento']] = medicamentos[diccionario['Medicamento']] + 1

    return medicamentos

#Función Comparar Pacientes
def CompararPacientes(tabla, IdPaciente1, IdPaciente2):
    resultado = {'Enfermedad': [], 'Medicamento': []}

    enfermedades = {}
    PacienteEnfermedad = {}
    ListaPacienteEnfermedad = []

    for diccionario in tabla:
        if diccionario['Identificacion'] in(IdPaciente1, IdPaciente2):
            PacienteEnfermedad = {'Idenfificacion: ': diccionario['Identificacion'], 'Enfermedad': diccionario['Enfermedad']}
            if PacienteEnfermedad not in(ListaPacienteEnfermedad):
                ListaPacienteEnfermedad.append(PacienteEnfermedad.copy())

    for diccionario in ListaPacienteEnfermedad:
        for clave in diccionario:
            if clave == 'Enfermedad':
                enfermedad = diccionario[clave]
                enfermedades[enfermedad] = 0

    for diccionario in ListaPacienteEnfermedad:   
        enfermedades[diccionario['Enfermedad']] = enfermedades[diccionario['Enfermedad']] + 1

    medicamentos = {}
    PacienteMedicamento = {}
    ListaPacienteMedicamento = []

    for diccionario in tabla:
        if diccionario['Identificacion'] in(IdPaciente1, IdPaciente2):
            PacienteMedicamento = {'Idenfificacion: ': diccionario['Identificacion'], 'Medicamento': diccionario['Medicamento']}
            if PacienteMedicamento not in(ListaPacienteMedicamento):
                ListaPacienteMedicamento.append(PacienteMedicamento.copy())

    for diccionario in ListaPacienteMedicamento:
        for clave in diccionario:
            if clave == 'Medicamento':
                medicamento = diccionario[clave]
                medicamentos[medicamento] = 0

    for diccionario in ListaPacienteMedicamento:   
        medicamentos[diccionario['Medicamento']] = medicamentos[diccionario['Medicamento']] + 1

    for clave in enfermedades:
        if enfermedades[clave] > 1:
            resultado['Enfermedad'].append(clave)

    for clave in medicamentos:
        if medicamentos[clave] > 1:
            resultado['Medicamento'].append(clave)
    
    return resultado


#Programa
print()
#Obtiene del archivo las recetas
Recetas = CargarTabla()

#Despliega en pantalla el resumen de enfermedades
ResumenEnfermedades = GenerarReporteEnfermedades(Recetas)
print('Resumen de Enfermedades')
print('Cantidad de pacientes por cada enfermedad')
for clave, valor in ResumenEnfermedades.items():
    print(clave + ': ' + str(valor))
print()

#Despliega en pantalla el resumen de medicamentos
ResumenMedicamentos = GenerarReporteMedicamentos(Recetas)
print('Resumen de Medicamentos')
print('Cantidad de pacientes por cada medicamento')
for clave, valor in ResumenMedicamentos.items():
    print(clave + ': ' + str(valor))
print()

#Despliega en pantalla la comparación entre dos pacientes
IdPaciente1 = '345'
IdPaciente2 = '456'
Comparacion = CompararPacientes(Recetas, IdPaciente1, IdPaciente2)
print('Comparación entre los pacientes ' + IdPaciente1 + ' y ' + IdPaciente2)
print('Enfermedades en común:')
if len(Comparacion['Enfermedad']) > 0:
    for elemento in Comparacion['Enfermedad']:
        print(elemento)
else:
    print('Ninguna')
print()
print('Medicamentos en común:')
if len(Comparacion['Medicamento']) > 0:
    for elemento in Comparacion['Medicamento']:
        print(elemento)
else:
    print('Ninguno')
print()
