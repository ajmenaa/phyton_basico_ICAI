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