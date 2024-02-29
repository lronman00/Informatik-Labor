error = False
import sys

try:
    temp = float(input("Geben Sie die Temperatur ein in beliebter Form:  "))
except:
    error = True

try:   
    art = int(input("1 = Celsius in Kelvin\n2 = Celsius in Fahreneinheit\n3 = Kelvin in Celsius\n4 = Kelvin in Fahreneinheit\n5 = Fahreneinheit in Celsius\n6 = Fahreneinheit in Kelvin:  "))
except:
    error = True

if error == True:
    print("Es ist was schief gelaufen")
    sys.exit()  # Programm beendet sich hier
    

elif art == 1:
    result  = temp - 273.15

elif art == 2:
    result = (temp * 9/5) + 32

elif art == 3:
    result = temp + 273.15

elif art == 4:
    result = (temp - 273,15) * 9/5 + 32

elif art == 5:
   result =  (temp - 32) * 5/9 

elif art == 6:
    result = (temp - 32) * 5/9 + 273,15

print(f"Ihr Ergebnis der Umrechnung ist {result}")

