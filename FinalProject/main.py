import streamlit as st
import pandas as pd

st.title ("Welcome to your Shotlist Organizer!")

# to get started: what is your project called?

x = st.text_input("What is the name of your project?", key="hey")
st.write(f"My Project is called {x}")

if x:
    st.badge("What a cute name!", color= "violet")
    st.session_state["x"] = x
    st.success(f"Gespeichert: {x}")

csv = st.text_input("Paste your csv path here")

if csv:
    df = pd.read_csv(csv)
    st.session_state["df"] = df
    st.success(f"Gespeichert: {csv}")

st.divider()

st.subheader("Choose your next step!")
st.divider()
st.page_link("pages/scene.py", label="Sort by *Scene!*")
st.divider()
st.page_link("pages/location.py", label="Sort by *Location!*")
st.divider()

# calculate overall shooting time

# select what you want to do now # sort by scene ? # sort by location