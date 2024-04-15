#Parte 2: Mini retos

#1. Marathon Time Calculator - 101 Computing


tiempo = input('Ingrese el tiempo en formato HH:MM')
Horas = int(tiempo[0:2])
Minutos = tiempo[-2:]
if Horas == 0:
    print (Horas = 12)  
else:
    print (Horas  ":" + Minutos + "am")

if Horas < 12:
    print (Horas + ":" + Minutos + "am")
    
if Horas == 12:
    print(Horas + ":" + Minutos + "pm")
    
if Horas < 24:
    print  (Horas = (Horas - 12))
else:
    print(Horas + ":" + Minutos + "pm")
