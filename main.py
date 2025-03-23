import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} {"day" if days < 2 else "days"} in {place}")

dates = ["2025-23-10", "2025-24-10", "2025-25-10"]

def get_data(number_of_days):
    temperatures = [10, 11, 15]
    temperatures = [number_of_days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(number_of_days=days)

labels = {
    "x": "Date",
    "y": "Temperature (C)"
}
figure = px.line(x=d, y=t, labels=labels)
st.plotly_chart(figure)