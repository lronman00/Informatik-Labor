name_box = "John Schnee"
age_box = "20"
uni_box = ""
subs_box = "1.99"
mkt_box = "0"


name_entered = bool(name_box)

if name_entered:
    name = name_box
else:
    name = "unknown"

age = int(age_box)
student = bool(uni_box)        #abfragen ob was in uni box steht mit 1 oder 0
subscripton = float(subs_box)   #1.99 mit nachkomma speichern
marketing = bool(int(mkt_box))  #

profile = (name + ', '
                + str(age) + ', '
                + str(student) + ', '
                + str(subscripton) + ', '
                + str(marketing))
print(profile)
