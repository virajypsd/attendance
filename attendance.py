import streamlit as st
import pandas as pd
import requests
import time

# Raspberry Pi Flask Server Address
RPI_SERVER = "http://192.168.0.168:5000/attendance"  # Change to your RPI IP

def load_data():
    """Fetch attendance data from the Raspberry Pi"""
    try:
        response = requests.get(RPI_SERVER)
        with open("attendance.csv", "wb") as f:
            f.write(response.content)
        return pd.read_csv("attendance.csv")
    except requests.exceptions.RequestException:
        return pd.DataFrame(columns=["Name", "Date", "Time", "Subject"])

st.title("📋 Face Recognition Attendance System")

# Auto-refresh every 5 seconds
while True:
    df = load_data()
    st.dataframe(df)
    time.sleep(5)  # Refresh data every 5 seconds
