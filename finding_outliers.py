

upper_limmit = 30
lower_limmit = 10

outlier = bool(False)

number = int(input("Wert eingeben: "))

if number > upper_limmit or number < lower_limmit:
    outlier = True


if outlier == True:
    print(f"{number} is a outliere")