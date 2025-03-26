import streamlit as st
import pandas as pd

# Set your Raspberry Pi's IP address here
RASPBERRY_PI_IP = "192.168.0.168"  # Change this to your actual IP
url = f"http://192.168.0.168:5000/get_attendance"

st.title("Real-time Attendance System")

st.write("### Attendance Records")

try:
    df = pd.read_csv(url)
    st.dataframe(df)  # Display attendance data in a table
except Exception as e:
    st.write("Error loading attendance records:", str(e))

st.write("Refresh the page to update attendance data.")
