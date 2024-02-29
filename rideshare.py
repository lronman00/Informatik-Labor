ride_type = (input("Wie möchten sie fahren? c = comfort / f = Fahrtenupgrade:  "))

string = (input("Wie viele Credits haben Sie?  "))

# if bool(string):
#     credits = int(string)
# else:
#     credits = 0

try:
    credits = int(string)
except:
    print("Credits set to 0")
    credits = 0


ride_price = 0
final_price = 0


if ride_type == "f":
    ride_price = 20.5
elif ride_type == "c":
    ride_price = 37.9
else:
    ride_price = 18.7

print(f"Fahrtyp: {ride_type} \nFahrtkosten: {ride_price} Euro")

if credits >= 0:
     final_price = ride_price - credits


print(f"Der Finale Preis nach Abzug der {credits} Credite sind {final_price} Euro")


