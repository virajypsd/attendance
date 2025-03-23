import streamlit as st
import pandas as pd
import requests

# Flask server IP (update if needed)
RPI_SERVER = "http://192.168.0.168:5000/attendance"

def load_data():
    try:
        response = requests.get(RPI_SERVER)
        response.raise_for_status()  # Raise error if request fails
        df = pd.read_json(response.text)  # Convert JSON to DataFrame
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=["Name", "Date", "Time", "Subject"])

st.title("📋 Face Recognition Attendance System")

# Load and display attendance data
df = load_data()
st.dataframe(df)  # Display data in a table
