import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} {"day" if days < 2 else "days"} in {place}")

dates = ["2025-23-10", "2025-24-10", "2025-25-10"]

try:
    if place:
        # Get the temperature/sky data
        # try can be used here too
        filtered_data = get_data(place, days)

        labels = {
            "x": "Date",
            "y": "Temperature (C)"
        }

        if option == "Temperature":
            # have to subtract by 273 since temp values are in kelvin
            temperatures = [int(dict["main"]["temp"]) - 273 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels=labels)
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # print(sky_conditions)
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.write(f"Sorry a place that goes by the name {place} cannot be found in our database :/")