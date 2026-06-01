import time
import random as rd
import csv
from datetime import datetime

DEBUG = True
#setup
if DEBUG:
    print("DEBUG MODE")
    name = input("What's your name?: ")
    clan_letter = rd.choice(["A", "B"])
    final_score = 0  # placeholder

#actual game
else:
    print("initiating game...")
    time.sleep(4)

    name = input("Before we start... Clasher, tell us your name. The fans are so curious...")
    time.sleep(1)
    print(f"Hello {name}! Another celebrity on our humble island.!")

    clan_letter = rd.choice(["A", "B"])
    print("Hm...")
    time.sleep(1)
    print(f"Oh wow! You are now and forever part of clan {clan_letter}! Have Fun")

    # begin of story
    time.sleep(5)
    print("A slight breeze hits your face.")
    time.sleep(2)
    print("It's only when you open your eyes that you realize... You were asleep.")
    time.sleep(2)
    print("You find yourself on a beach. In the distance, a voice is speaking but it sounds like an echo from the past...")
    time.sleep(2)
    print("'Everyone else must die'")

    # dictionary beach
    beach_items = [
        {"name": "shells", "type": "trinkets", "points": 1},
        {"name": "minecraft sword", "type": "weapon", "points": 2, "description": "why would this sword be on a random island..."},
        {"name": "bloody mask", "type": "artifact", "points": 5, "description": "What do we have here..... This was worn by the first true winner. His sacrifice was so noble."},
    ]

    # dictionary forest
    forest_items = [
        {"name": "special cake", "type": "Food", "points": 10, "description": "The cake has an old note on it... You can only make out the word 'wookie'. \n We are not in Star Wars though?"},
        {"name": "bandana", "type": "artifact", "points": 4, "description": "A bandana worn by the masked man's lover"},
        {"name": "schmedgar the pig", "type": "danger", "points": -1, "description": "A traitorous cute looking pig..."},
        {"name": "berries", "type": "danger", "points": -3},
    ]

    # story
    time.sleep(7)
    fate = input("Ignore all that, Clasher! Instead choose where you want to go?\n"
                 "Beach \n"
                 "Forest \n"
                 "Please write it out.").strip().lower()
    print(f"So you want to go to the {fate}... Interesting {name} from Clan {clan_letter}.\n In order to survive the new version of this challenge, you must simply reach 12 points.")

    if fate == "forest":
        current_room = "forest"
        items_in_room = forest_items
    else:
        current_room = "beach"
        items_in_room = beach_items

    # current state of the game
    inventory = []

    # functions
    def show_inventory():
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for item in inventory:
                print(f"{item['name']}: {item['type']}: {item['points']}")

    def show_room_items():
        print(f"You look around the {current_room}:")
        if len(items_in_room) == 0:
            print("Nothing here. This island used to be so lively...")
        else:
            for item in items_in_room:
                print(f"{item['name']}")

    def pick_up(item_name):
        if len(inventory) >= 5:
            print("Inventory full! Drop something first.")
            return
        for item in items_in_room:
            if item["name"] == item_name:
                inventory.append(item)
                items_in_room.remove(item)
                print(f"Picked up {item_name}.")
                return
        print(f"No '{item_name}' here.")

    def drop(item_name):
        for item in inventory:
            if item["name"] == item_name:
                inventory.remove(item)
                items_in_room.append(item)
                print(f"Dropped {item_name}.")
                return
        print(f"You don't have '{item_name}'.")

    def examine(item_name):
        for item in inventory:
            if item["name"] == item_name:
                print(f"{item_name} is a {item['type']}.")
                if "description" in item:
                    print(item["description"])
                return
        print(f"You don't have '{item_name}'.")

    def points(item_name):
        for item in inventory:
            if item["name"] == item_name:
                print(f"{item_name} is worth {item['points']} points.")
                return
        print(f"You don't have '{item_name}'.")

    # main game
    print("Commands: look, inventory, pickup, drop, examine, points, move, quit")

    while True:
        command = input("What do you do? ")

        if command == "look":
            show_room_items()

        elif command == "inventory":
            show_inventory()

        elif command == "move":
            if current_room == "beach":
                current_room = "forest"
                items_in_room = forest_items
            else:
                current_room = "beach"
                items_in_room = beach_items
            print(f"You move to the {current_room}.")

        elif command == "quit":
            break

        elif command == "pickup":
            item_name = input("What do you want to pick up? ")
            pick_up(item_name)

        elif command == "drop":
            item_name = input("What do you want to drop? ")
            drop(item_name)

        elif command == "examine":
            item_name = input("What do you want to examine? ")
            examine(item_name)

        elif command == "points":
            item_name = input("Which item? ")
            points(item_name)

        total = 0
        for item in inventory:
            total += item["points"]
        if total >= 12:
            print(f"You reached 12 points! Clan {clan_letter} wins, {name}!")
            break
        if total <= -3:
            print("Too many bad items... you didn't survive.")
            break

    final_score = total

# save stats

timestamp = str(datetime.now())[:16]

# look at stats
try:
    with open("records.csv") as file:
        reader = csv.reader(file)
        records = []
        for row in reader:
            records.append(row)
    print("Existing records loaded.")
except FileNotFoundError:
    records = [["Name", "Clan", "Score", "Timestamp"]]
    print("No record file found. Creating a new one.")

# add current result
records.append([name, clan_letter, final_score, timestamp])

# cvs
try:
    with open("records.csv", "w", newline="") as file: #this line i had help with AI
        writer = csv.writer(file)
        writer.writerows(records)
    print("Your result has been saved!")
except Exception as e:
    print(f"Could not save records: {e}")

# leaderboard

# separate the header from the data rows
header = records[0]
data_rows = records[1:]

for i in range(len(data_rows)):
    for j in range(i + 1, len(data_rows)):
        if int(data_rows[i][2]) < int(data_rows[j][2]): #help from AI
            data_rows[i], data_rows[j] = data_rows[j], data_rows[i]

print("\n ---LEADERBOARD--- ") #from here on also help with AI
print(f"{'Name':<15} {'Clan':<6} {'Score':<7} {'Timestamp'}")
print("-" * 45)
for row in data_rows:
    print(f"{row[0]:<15} {row[1]:<6} {row[2]:<7} {row[3]}")