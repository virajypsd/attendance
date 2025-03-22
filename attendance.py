import streamlit as st
import pandas as pd
import requests

# URL of the Raspberry Pi API (Replace with actual IP)
RPI_SERVER = "http://192.168.0.168:5000/attendance"  # Change to your RPI IP

def load_data():
    try:
        response = requests.get(RPI_SERVER)
        with open("attendance.csv", "wb") as f:
            f.write(response.content)
        return pd.read_csv("attendance.csv")
    except:
        return pd.DataFrame(columns=["Name", "Date", "Time", "Subject"])

st.title("📋 Face Recognition Attendance System")

# Load data
df = load_data()

# Display table
st.write(df)
