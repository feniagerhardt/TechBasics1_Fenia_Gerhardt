import random
from turtle import *
from batman import batman_logo

print("Hello, this is the Gotham Police Department.")
name = input("What is your name? ")
print("Hello, " + name)
villain = input("""Because of which villain are you calling? 
Joker, Scarecrow, Riddler, Red Hood, Penguin""" )

if villain.lower() == "joker":
    ernsthaftigkeit = 5
    print ("We need all hands on deck!")
elif villain.lower() == "scarecrow" or villain.lower() == "riddler" or villain.lower() == "penguin":
    ernsthaftigkeit = 3
    print ("This is NOT good!")
elif villain.lower() == "red hood":
    ernsthaftigkeit = 0
    print ("Not again! They argue every day, we should send a family therapist instead... But")
else:
    ernsthaftigkeit = 1
    print ("Oh this happens all the time...")

anzahl = random.randint(ernsthaftigkeit, ernsthaftigkeit +3)
print (f"We need to light the Batsignal {anzahl} times for this!")

for i in range(anzahl):
    x = random.randint(-300,300)
    y = random.randint(-200,200)
    batman_logo(x,y)

done()