import streamlit as st
import pandas as pd

def image_creation():
    image = st.text_input ("Paste the URL to your image")
    if image:
        st.image(image)
        st.badge("Good job!!", color="green")
        st.session_state["image"] = image
    else:
        st.badge("No image yet!! Add one above👾", color="red")

def click_button():
    is_clicked = st.button("Click me!!✌🏻")
    if is_clicked:
        st.badge("You've updated the page!")

def add_line_button(key_suffix):
    toggle_key = f"show_form_{key_suffix}"

    if toggle_key not in st.session_state:
        st.session_state[toggle_key] = False

    if st.button("Add line", key=f"toggle_{key_suffix}"):
        st.session_state[toggle_key] = True

    if st.session_state[toggle_key]:
        new_location = st.text_input("Location", key=f"location_{key_suffix}")
        new_scene = st.number_input("Scene", key=f"scene_{key_suffix}")
        new_shot_number = st.number_input("Shot Number", key=f"shotnumber_{key_suffix}")

        if st.button("Save", key=f"save_{key_suffix}"):
            if new_location and new_scene:
                current_df = st.session_state.get("df")
                new_row = pd.DataFrame([{
                    "Location": new_location.strip(),
                    "Scene": new_scene,
                    "Shot Number": new_shot_number
                }])
                st.session_state["df"] = pd.concat([current_df, new_row], ignore_index=True)
                st.session_state[toggle_key] = False
                st.rerun()
        else:
            st.warning ("Please put in all values")

