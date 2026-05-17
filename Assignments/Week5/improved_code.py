#Song Mood Supporter

#importing 1 library

import random

#setting up dictionaries for structure, readability and more flexibility

anger = ["not like us by kendrick lamar", "you thought by hannah geller", "silver spoon by bts", "ugh by bts", "the last by agust d", "set me free pt.2 by jm",]
sad = ["hard times by ethel cain", "straw house by jade", "blue & grey by bts", "falling by harry styles", "this is me trying by taylor swift", "waking in the dark by only the poets"]
happy = ["loud by NMIXX", "dover beach by baby queen", "the spark by louis tomlinson", "one more night by only the poets", "what it sounds like by huntr/x", "out of my system by louis tomlinson"]
unsure = ["wild flower by RM", "golden by harry styles", "interlude:shadow by bts", "shatter me by lindsey stirling", "lucid by louis tomlinson", "runaway by aurora"]

#replacing conditionals with 1 function

def recommend_songs(emotion, mood):
    playlists = {"angry": anger, "sad": sad, "happy": happy, "unsure": unsure}
    return random.sample(playlists.get(emotion, unsure), mood // 3 + 1) #scale now decides the number of songs recommended #i love randomness

#putting everything into a main function

def main():
    print("welcome to your musical mood therapist!")
    emotion = input(""" what emotion are you feeling the most right now? 
        angry/sad/happy/unsure """) #shortening the questions part of the code
    mood = int(input(f"On a scale from 1 to 10, how much are you feeling {emotion} right now?")) #answer is an integer / no need for string libraries now

    if emotion not in {"angry", "sad", "happy", "unsure"}:
        print("i see you're trying to break the system... Spine Breaker by BTS is for you. Now please answer correctly") #typo conditional/failsafe #this is a great song btw
        return

    print(f"\nhere are your songs for today: {recommend_songs(emotion, mood)}")

main()