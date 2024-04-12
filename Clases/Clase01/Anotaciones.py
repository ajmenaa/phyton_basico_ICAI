#comentarios

"""comentarios"""

"""
comentarios
multilinea

"""

print ('Hola'); # esto es un mensaje de bienvenida
print ("""Linea 1  
       Linea 2
        Linea 3  
""")# comentario multilinea


linea2='\n Programa clase 1'
linea1='\n Programa clase 1'
print (linea2 + 'xxx')
print (linea2 , 'xxx')

numero=122
numero2=233.4
bandera= True
print (type(numero))
print (type(linea1))
print (type(bandera))
print (type(numero2))


#assignacion en tupla
bandera, numero, numero2= True, 3,3.4

nombre= input ('Cual es tu nombre')
print (nombre)

print (f"Bienvenido: (nombre), su edad es ")

suma= 1+2
print (f"la suma es: {suma}")
divisionEntera= 10//3
print (f"la division entera es: {divisionEntera}")


divisionModular= 10%3
print (f"la division entera es: {divisionModular}")