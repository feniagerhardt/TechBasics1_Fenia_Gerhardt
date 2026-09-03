import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) #AI

from shared_functions import click_button, image_creation
from main import space

# access title / test to check if cross save works

x = st.session_state.get("x", "")

# title depending on the scenario

if x:
    st.title(f" ✨Shotlist Organizer for {x} / Scene✨")
else:
    st.title("Shotlist Organizer / Scene")

# functions

click_button()
space()
image_creation()
space()

# get data from homepage (this is difficult ahh)

df = st.session_state.get("df", "")

if df is not None:
    scene_options = df["Scene"].unique().tolist()

    sortscene = st.select_slider("Which scene are you looking for?", options=scene_options)
    st.write("Here is the", sortscene, "scene")
    filtering = df[df["Scene"] == sortscene]
    st.data_editor(filtering)

space()

# daytime slider bar

# this code is ugly, i will put it differently later
daytime_images = {
    "night": "FinalProject/night.jpeg", "midday": "FinalProject/midday.jpg","sunrise": "FinalProject/sunrise.jpg","golden hour": "FinalProject/golden hour.jpeg","evening": "FinalProject/evening.jpg.avif", "afternoon": "FinalProject/afternoon.jpg.avif","after midnight": "FinalProject/after midnight.jpeg", "morning": "FinalProject/early morning.jpg", "late morning": "FinalProject/late morning.jpeg",
}

daytime = st.select_slider(
    "When does your scene take place?🌙",
    options=[
        "after midnight","sunrise", "morning","late morning", "midday","afternoon", "golden hour","evening","night",
    ],
)
st.write("The scene takes place at this time", daytime)

left_co, cent_co, last_co = st.columns(3) # from streamlit q&a
with cent_co:
    if daytime in daytime_images:
        st.image(daytime_images[daytime], width=400)
    else:
        st.badge("Sadly no picture!", color="red")

# edit dataframe with widgets ?

st.divider()

# choosing specific shot

def edit_shotlist():
    if df is not None:
        shot_options = filtering["Shot Number"].unique().tolist()  # AI so it accesses the scene not the entire df
        numbershot = st.selectbox("Shot Number?", shot_options)
        st.write("You chose Shot Number:", numbershot)
        final_filter = filtering[filtering["Shot Number"] == numbershot]
        st.data_editor(final_filter)

    # widgets (** need to change data_editor, add s.session_state stuff)

    col1, col2 = st.columns(2)
    with col1:
        camera_movement = ["Static", "Tracking", "Handheld"] # simulate movement or smth if there is time
        click2 = st.selectbox("Camera Movement?", camera_movement)
        if click2:
            st.session_state["click2"] = click2
            st.success(f"Gespeichert: {click2}") # this is also ugly

    with col2:
        pov_chooser = ["MCU (Medium Close Up)", "MS (Medium Shot)", "OTS (Over the shoulder)", "WS (Wide Shot)", "CU (Close Up)", "FS (Full Shot)"]
        click = st.selectbox("Shot Size?", pov_chooser)
        if click:
            st.session_state["click"] = click
            st.success(f"Gespeichert: {click}")
        if click == "MCU (Medium Close Up)":
            st.badge("Simple but effective", color="green")
        elif click == "MS (Medium Shot)":
            st.snow()                                   # to remember that this exists later haha
#        elif click == "OTS (Over the shoulder)":
#            st.image("/Users/feniacelina/Downloads/Red Hood.webp") # local placeholder


    gear_choice = ["Handheld", "Tripod", "Handheld Rig", "Gimbal", "Steadicam", "Shoulder Rig"]
    click3 = st.selectbox("Gear?", gear_choice)
    if click3:
        st.session_state["click3"] = click3
        st.success(f"Gespeichert: {click3}")

edit_shotlist()

# description / note box



