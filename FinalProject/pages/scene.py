import streamlit as st
import pandas as pd

x = st.session_state.get("x", "")

if x:
    st.title(f" ✨Shotlist Organizer for {x} / Scene✨")
else:
    st.title("Shotlist Organizer / Scene")

is_clicked = st.button("Click me")
if is_clicked:
    st.write("OMG so cool!")
    st.badge("Good job!!", color="green")

# paste url and get image / work on making this more user-friendly / maybe add a save option

imagecreation = st.text_input ("Paste the URL to your image")
if imagecreation:
    st.image(imagecreation)
    st.badge("Good job!!", color="green")
else:
    st.badge("No image yet!! Add one above👾", color="red")

# get data from homepage (this is difficult ahh)

df = st.session_state.get("df", "")

if df is not None:
    sortscene = st.slider("Which scene are you looking for?", 1, 8, 4)
    st.write("Here is the", sortscene, ") scene")

    filtering = df[df["Scene"] == sortscene]
    st.data_editor(filtering)

# daytime slider bar

daytime = st.select_slider(
    "When does your scene take place?🌙",
    options=[
        "after midnight🌌",
        "sunrise🌄",
        "morning⛅️",
        "late morning",
        "midday☀️",
        "afternoon",
        "evening",
        "night",
    ],
)
st.write("The scene takes place at this time", daytime)

# edit dataframe with widgets ?

pov_chooser = ["MCU (Medium Close Up)", "MS (Medium Shot)", "OTS (Over the shoulder)", "WS (Wide Shot)"]
click = st.menu_button("camera perspective?", pov_chooser)
if click == "MCU (Medium Close Up)":
    st.badge("Simple but effective", color="green")
elif click == "MS (Medium Shot)":
    st.snow()                                   # to remember that this exists later haha
elif click == "OTS (Over the shoulder)":
    st.image("/Users/feniacelina/Downloads/Red Hood.webp") # local placeholder

# use pandas more to look at different colums / make it choosable / look into how to use pandas x streamlit properly

# description box

# simulate movement ( gifs / videos ? )


