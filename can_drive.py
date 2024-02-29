can_drive = False
has_license = False

age = int (input("Was ist dein Alter: "))
has_license = (input("Has license? Ja / Nein: "))
versicherung = input("Hast du eine Versicherung? Ja / Nein : ")
pre_license = input("Has pre license? Ja / Nein ")

limit_age = age >= 18

if  (limit_age) and ((has_license == "Ja") or \
    (pre_license == "Ja")) and (versicherung == "Ja"):          # not negieren
    can_drive = True

else:
    can_drive = False
   
   
   
print(can_drive)