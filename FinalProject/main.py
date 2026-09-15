import streamlit as st
import pandas as pd

st.title("Welcome to your Shotlist Organizer!")

# introduction: asking for name

x = st.text_input("What is the name of your project?", key="hey")

# reaction and save session

if x:
    st.header(f"My Project is called {x}")
    st.badge("What a cute name!", color= "violet")
    st.session_state["x"] = x
    left_co, cent_co, last_co = st.columns(3)
    with last_co:
        st.image("https://i.pinimg.com/originals/de/43/2d/de432d8cbf2650748a69a224f4f9d244.gif", width=200)


# defining function

def space():
    st.text("")
    st.text("")

space()

# informing user of necessary steps

st.subheader("Before we start:")
st.markdown("""
Do you have a File already? If not:
1. Open an Excel file and create/change the categories for your shotlist!
2. Make sure they are named exactly like this: **"Scene"**, **"Location"** :)
3. Save this file as a CSV and look below :)
""")
# saving csv file for cross page use

csv = st.text_input("Paste your csv path here")

if csv:
    df = pd.read_csv(csv, sep=None, engine="python", encoding="utf-8")
    if len(df.columns) == 1:
        df = pd.read_csv(csv, sep=";")          # i figured out the problem my code is fixing here with AI
    st.session_state["df"] = df
    st.success(f"Saved: {csv}")
    #st.write(df.columns.tolist()) #activate if csv df does not work
space ()

# choose the next page / sort by location vs scene

st.markdown("<hr style='border:1px solid #8A5FBF;'>", unsafe_allow_html=True)
st.subheader("Would you rather...")

col1, col2=st.columns(2) # put it next to each other
with col1:
    st.page_link("pages/scene.py", label="Sort by *Scene!*")
with col2:
    st.page_link("pages/location.py", label="Sort by *Location!*")
st.markdown("<hr style='border:1px solid #8A5FBF;'>", unsafe_allow_html=True)
