import time
print("Welcome to your mood saver! BTS beta edition")
mood = input("On a scale from 1 to 10, how are you feeling right now? ")

m1 = ("1", "2", "3")
m2 = ("4", "5", "6")
m3 = ("7", "8", "9", "10")

if mood in m1:
    print("Oh Shit")
    question = input("Do you want sad songs right now? Yes or No? ").strip().lower()
    if question == "Yes":
        print("You should listen to Blue & Grey by BTS")

    question2 = input("Do you want angry songs right now? Yes or No? ").strip().lower()
    if question2 == "Yes":
        print("You should listen to Cypher Pt. 3 or UGH by BTS")

    question3 = input("Do you want to be HYPED UP? Yes or No? ").strip().lower()
    if question3 == "Yes":
        print("You should listen to Idol by BTS")

elif mood in m2:
    print("I don't know what to tell you. Hope you feel better soon!")
    question4 = input("Do you like Rap? Yes or No").strip().lower()
    if question4 == "Yes":
        print("You should listen to The Last by Agust D")
    question5 = input("Do you like sad ballads? Yes or No").strip().lower()
    if question5 == "Yes":
        print("You should listen to ")
    question6 = input("Do you feel lost right now? Yes or No? ").strip().lower()
    if question6 == "Yes":
        print("You should listen to Wild Flower by RM")
    else:
        time.sleep (3)
        print ("I don't know how to help you! Goodbye!")

elif mood in m3:
    print("Omg yay, that's amazing!!")
    question7 = input("Do you want songs that make you feel powerful? Yes or No? ").strip().lower()
    if question7 == "Yes":
        print("You should listen to Set Me Free by JIMIN or The Last by Agust D")
    else:
        print ("Listen to Like Animals by BTS on ARIRANG!")

else:
    print("I see you are trying to resist the system. Spine Breaker by BTS is for you. Now please enter a correct number")