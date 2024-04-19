
#Programa que lea un archivo que indique el usuario
#Si el archivo no existe le notificamos al usario
#Y si si existe le agregamos el texto que diga el usario

import os


def prueba():
    pass      # pass es un comeando de escape para una funcion no conclusa
# es como una instruccion nula

def leerArchivo():
    pass      

def agregarArchivo():
    try:
         ruta= os.path.joi("Estudiantes","Karol_Leiton","Semana3", nombreArchivo)
        with open(ruta, 'w')as archivo:
            
   


#--------------------------------------------

#intentar leer el archivo
def leerArchivo (nombreArchivo):
    #""" funcion para leer un archivo cuyo nombre recibo por parametro
      try:
          ruta= os.path.joi("Estudiantes","Karol_Leiton","Semana3", nombreArchivo)
          with open (nombreArchivo, 'r') as archivo:
              contenido=archivo.read() # el contenido del archivo se asigna a la variable
              return contenido
      except FileNotFoundError:
          return ""
    #--------------------------------------
nombreArchivo=input ('el nombre del archivo a leer: ')
textoArchivo=input ('ingrese el mensaje')
contenidoLeido=leerArchivo(nombreArchivo)
print(contenidoLeido)

if not contenidoLeido:
    print ('archivo no encontrado')
    #agregarArt
else:
    print ('el contenido del arhivo es :', contenidoLeido)

    