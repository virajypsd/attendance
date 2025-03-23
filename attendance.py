import streamlit as st
import pandas as pd
import requests

# Flask server IP (Replace with your actual Raspberry Pi IP)
RPI_SERVER = "http://192.168.0.168:5000/attendance"

def fetch_attendance():
    """Fetch attendance data from the Raspberry Pi Flask server."""
    try:
        response = requests.get(RPI_SERVER)
        response.raise_for_status()  # Raise error if request fails
        data = response.json()  # Parse JSON response
        return pd.DataFrame(data)  # Convert to DataFrame
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame(columns=["Name", "Date", "Time", "Subject"])

# Streamlit Page Config
st.set_page_config(page_title="Face Recognition Attendance", layout="wide")

# Title
st.title("📋 Face Recognition Attendance System")

# Load data
df = fetch_attendance()

# Display Data
if not df.empty:
    st.dataframe(df, use_container_width=True)  # Show table in full width
else:
    st.warning("No attendance data available.")

# Refresh Button
if st.button("🔄 Refresh Data"):
    df = fetch_attendance()
    st.experimental_rerun()
