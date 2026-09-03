import streamlit as st
import pandas as pd

st.title ("Welcome to your Shotlist Organizer!")

# introduction: asking for name

x = st.text_input("What is the name of your project?", key="hey")
st.write(f"My Project is called {x}")

# reaction and save session

if x:
    st.badge("What a cute name!", color= "violet")
    st.session_state["x"] = x
    st.success(f"Gespeichert: {x}")

# defining function

def space():
    st.text("")
    st.text("")

space()

# informing user of necessary steps

st.subheader("Before we start:")
st.write("""
    Do you have a File already?
    1) Open an Excel file and create/change the categories for your shotlist!
    2) Make sure they are named exactly like this: "Scene", "Location" :)
    4) Save this file as a CSV and look below :)
    """)

space()

# saving csv file for cross page use

csv = st.text_input("Paste your csv path here")

if csv:
    df = pd.read_csv(csv)
    st.session_state["df"] = df
    st.success(f"Gespeichert: {csv}")

space ()

# choose the next page / sort by location vs scene

st.subheader("Would you rather...?")
st.divider()

col1, col2=st.columns(2) # put it next to each other
with col1:
    st.page_link("pages/scene.py", label="Sort by *Scene!*")
with col2:
    st.page_link("pages/location.py", label="Sort by *Location!*")
st.divider()

