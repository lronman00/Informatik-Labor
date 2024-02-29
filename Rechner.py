error = False


try:
    zahl1 = float(input("Wert Zahl 1 eingeben: "))
except:
     error = True
try:     
    zahl2 = float(input("Wert Zahl 2 eingeben: "))
except:
     error = True

if error == True:
     print("Irgendwas ist schief gelaufen")

operation = (input(" (+) /  (-) / (*) /  (/): "))
print("\n\n")


if operation == '/':
        try:
            result = zahl1 / zahl2
            print(f"Ergebnis der Division ist {result}\n\n")
        except ZeroDivisionError:
            print("Division durch Null ist nicht erlaubt.")

elif operation == '+':
    result = zahl1 + zahl2
    print(f"Ergebnis der Addition ist {result}\n\n")

elif operation == '-':
    result = zahl1 - zahl2
    print(f"Ergebnis der Subtraktion ist {result}\n\n")

elif operation == '*':
    result = zahl1 * zahl2
    print(f"Ergebnis der Multiplikation ist {result}\n\n")

else:
    print("Operation ist nicht unterstützt")


