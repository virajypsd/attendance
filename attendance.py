import streamlit as st
import pandas as pd
import os
import requests
from datetime import datetime

# File to store attendance
ATTENDANCE_FILE = "attendance.csv"
API_URL = "http://your-raspberry-pi-ip:5000/attendance"  # Replace with actual API endpoint

# Function to load attendance data
def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        return pd.read_csv(ATTENDANCE_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Date", "Time"])

# Function to save attendance data
def save_attendance(df):
    df.to_csv(ATTENDANCE_FILE, index=False)

# Function to fetch attendance data from API
def fetch_attendance_from_api():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            st.error("Failed to fetch attendance from API")
            return load_attendance()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return load_attendance()

# Streamlit UI
st.title("📋 Attendance Management System")

# Fetch and display attendance from API
st.subheader("📊 Attendance Records (API Fetched)")
attendance_data = fetch_attendance_from_api()
st.dataframe(attendance_data)
