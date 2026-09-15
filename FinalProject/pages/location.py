import streamlit as st
import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # AI
from fpdf import FPDF

from shared_functions import click_button, image_creation, add_line_button
from main import space

def safe_text(text): # this function is with ai
    if not isinstance(text, str):
        text = str(text)
    text = text.replace('\ufeff', '').replace('\ufffe', '')  # strip BOM
    return text.encode('latin-1', errors='replace').decode('latin-1')

x = st.session_state.get("x", "")

if x:
    st.title(f" ✨Shotlist Organizer for {x} / Location✨")
else:
    st.title("Shotlist Organizer / Location")

space()
image_creation()
space()

# get data from homepage

df = st.session_state.get("df", None)
filtering = None

if df is not None and not df.empty:
    location_options = df["Location"].unique().tolist()

    sortlocation = st.select_slider("Which Location are you looking for?", options=location_options)
    st.write("Ah so this scene is happening there!", sortlocation)
    filtering = df[df["Location"] == sortlocation]
    st.data_editor(filtering)
    st.session_state["location"] = sortlocation
    add_line_button(key_suffix="normal_list")
else:
    st.info("Your shotlist is empty! Add a few lines")
    save_line = add_line_button(key_suffix="empty_shotlist")
    st.session_state["save_line"] = save_line

space()

# daytime slider bar

daytime_images = {
    "night": "FinalProject/pictures/night.jpeg", "midday": "FinalProject/pictures/midday.jpg","sunrise": "FinalProject/pictures/sunrise.jpg","golden hour": "FinalProject/pictures/golden hour.jpeg","evening": "FinalProject/pictures/evening.jpg.avif", "afternoon": "FinalProject/pictures/afternoon.jpg.avif","after midnight": "FinalProject/pictures/after midnight.jpeg", "morning": "FinalProject/pictures/early morning.jpg", "late morning": "FinalProject/pictures/late morning.jpeg",
}

daytime = st.select_slider(
    "When does your scene take place?🌙",
    options=[
        "after midnight", "sunrise","morning","late morning", "midday","afternoon","golden hour","evening","night",
    ],
)
st.session_state["daytime"] = daytime
st.write("The scene takes place at this time", daytime)

left_co, cent_co, last_co = st.columns(3) # from streamlit q&a
with cent_co:
    if daytime in daytime_images:
        st.image(daytime_images[daytime], width=400)
    else:
        st.badge("Sadly no picture!", color="red")


# edit dataframe with widgets ?

st.divider()

final_filter = None

def current_status():
    current_location = st.session_state.get("location", "")
    current_shot = st.session_state.get("numbershot", "")
    return current_location, current_shot

if df is not None and filtering is not None:
    shot_options = filtering["Shot Number"].unique().tolist()  # AI so it accesses the scene not the entire df
    numbershot = st.selectbox("Shot Number?", shot_options)

    st.write("You chose Shot Number:", numbershot)
    final_filter = filtering[filtering["Shot Number"] == numbershot]
    st.session_state["numbershot"] = numbershot

    widgets_editor = {
        "Camera Movement": ["Static", "Tracking", "Handheld"],
        "Shot Size": ["MS (Medium Shot)", "MCU (Medium Close Up)", "OTS (Over the shoulder)", "WS (Wide Shot)", "CU (Close Up)", "FS (Full Shot)"],
        "Gear": ["Handheld", "Tripod", "Handheld Rig", "Gimbal", "Steadicam", "Shoulder Rig"],
    }

    # trying to make it less repetitive
    current_location, current_shot = current_status()
    locator = (df["Location"] == current_location) & (df["Shot Number"] == current_shot)

    col1, col2 = st.columns(2)
    with col1:
        click2 = st.selectbox("Camera Movement?", widgets_editor["Camera Movement"]) #movement illustration would be cool

        if click2:
            current_location, current_shot = current_status()
            if current_location is not None and current_shot is not None:
                df.loc[locator, "Camera Movement"] = click2
                st.session_state["click2"] = click2
                st.session_state["df"] = df

    with col2:
        click = st.selectbox("Shot Size?", widgets_editor["Shot Size"])

        if click:
            current_location, current_shot = current_status()
            if current_location is not None and current_shot is not None:
                df.loc[locator, "Shot Size"] = click
                st.session_state["click"] = click
                st.session_state["df"] = df
            else:
                st.warning("Did you select a shot?")

        if click == "MCU (Medium Close Up)":
            st.badge("Simple but effective", color="violet")

    # gear choice

    click3 = st.selectbox("Gear?", widgets_editor["Gear"])

    if click3:
        current_location, current_shot = current_status()
        if current_location is not None and current_shot is not None:
            df.loc[locator, "Gear"] = click3
            st.session_state["click3"] = click3
            st.session_state["df"] = df

    st.write("This line was changed:")
    st.data_editor(final_filter, key= "Changed")
    st.divider()
    st.write("Changes not updating?")
    click_button()
    st.divider()

    def build_pdf(dataframe: pd.DataFrame) -> bytes: # this is AI because i was so confused
        pdf = FPDF()
        pdf.add_page()

        # this is not ai anymore
        for scene_name, scene_df in dataframe.groupby("Scene"):
            # Scene header
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 10, safe_text(f"Scene: {scene_name}"), ln=True)

            for _, row in scene_df.iterrows():
                pdf.set_font("Helvetica", "", 11)
                for col in scene_df.columns:
                    if col == "Scene":
                        continue
                    pdf.cell(0, 7, safe_text(f"{col}: {row[col]}"), ln=True)
                pdf.ln(4)

            pdf.ln(8)

        # this is ai
        raw = pdf.output(dest='S')
        return raw.encode('latin-1') if isinstance(raw, str) else bytes(raw)

    # this is not
    if df is not None and not df.empty:
        csv_export = df.to_csv(index=False)
        pdf_export = build_pdf(df)

        st.download_button(
            label="Download as CSV",
            data=csv_export,
            file_name="updated_csv_hotlist.csv",
            mime="text/csv"
        )
        st.download_button(
            label="Download as PDF",
            data=pdf_export,
            file_name="updated_pdf_shotlist.pdf",
            mime="application/pdf"
        )