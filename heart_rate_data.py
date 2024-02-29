print("Bitte geben sie eine Herzfrequenz ein")
heart_rate_var = int(input())

if heart_rate_var < 60:
    print("Herzfrequenz zu niedrig")
elif heart_rate_var > 100:
    print("Herzfrequenz zu hoch")
elif heart_rate_var > 60 and heart_rate_var < 100:
    print("Alles ist Gut")

input() # lässt das Window open