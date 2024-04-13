
#Programa Area del triagulo
Base = input("Digite la medida de la base del triagulo: ")

Altura = input("Digite la medida de la altura del triagulo: ")

Area = (int(Base) * int(Altura)) / 2 #Calcula area del triagulo en base a las medidas introducidas por el usuario

print(f"El area del triangulo es: {int(Area)}")


#Programa conversion Dolares a Colones
TipoCambio = 500

print(f"El tipo de cambio actual es de ¢{TipoCambio} por cada $ Dolar")

Cantidad_Dolares = input("Digite la catidad de Dolares que desea convertir: $")

Conversion = int(Cantidad_Dolares) * TipoCambio

print(f"La cantidad de colones despues de la conversion es: ¢{Conversion}")


#Programa convertir grados centigrados a fahrenheit 
GradosC = input("Digite los grados centigrados que desea convertir a fahrenheit: ")

GradosF = (float(GradosC) * 1.8) + 32

Resp_redondeada = str(round(GradosF, 2))

print(f"Los grados fahrenheit son: {Resp_redondeada}")


#Marathon Time Calucultor - www.101computing.net/marathon

#Step 1: INPUT: Ask the runner for their pace (e.g. 5:25)
str_pace = input("At what pace do you run a km? (e.g. 5:21): ")

#Step 2: PROCESS: Convert this input into a number of seconds: e.g. 5:25 = 5 * 60 + 25 = 325 seconds
#...

minutes = int(str_pace[:1])

seconds = int(str_pace[-2:])

total_secs = (minutes * 60) + seconds

#Step 3: PROCESS: Multiply this total by 42 as there are 42km in a Marathon
#...
totalTime = total_secs * 42

#Step 4: PROCESS: Convert this new total using the hh:mm:ss format. (e.g 3:47:30)
#...
# Get minutes and seconds
mm, ss = divmod(totalTime, 60)

# Get hours and minutes
hh, mm = divmod(mm, 60)

#Step 5: OUTPUT: Display this new total on screen (using the hh:mm:ss format). (e.g 3:47:30)
#...
#print(f"The total time is: {totalTime}")
print(f"Time in hh:mm:ss: {hh}:{mm}:{ss}")


#Time Conversiobr - www.101computing.net/time-conversion/ 

time = input("Enter a time in the hh:mm format (e.g 18:36): ")

#Complete the code here...

hours = int(time[:2])

minutes = int(time[-2:])

#print(hours,minutes)

if hours == 0:
    hours = 12
    print(f"{hours}:{minutes} am")
elif hours < 12:
    print(f"{hours}:{minutes} am")
elif hours == 12:
    print(f"{hours}:{minutes} pm")
elif hours < 24:
    hours = hours - 12
    print(f"{hours}:{minutes} pm")










