import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the "
                                                                 "number of "
                                                                 "days you "
                                                                 "want to "
                                                                 "forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10"]
temperature = [10, 15, 18, 12, 15]
figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperatue (C)"})
st.plotly_chart(figure)