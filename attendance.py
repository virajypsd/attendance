import streamlit as st
import pandas as pd
from datetime import datetime
import os

# File to store attendance data
ATTENDANCE_FILE = "attendance.csv"

# Initialize attendance file if not exists
def init_file():
    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=["Name", "Date", "Time"])
        df.to_csv(ATTENDANCE_FILE, index=False)

# Function to mark attendance
def mark_attendance(name):
    df = pd.read_csv(ATTENDANCE_FILE)
    now = datetime.now()
    new_entry = pd.DataFrame([[name, now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S')]], columns=["Name", "Date", "Time"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(ATTENDANCE_FILE, index=False)
    st.success(f"Attendance marked for {name}")

# Function to load attendance records
def load_attendance():
    return pd.read_csv(ATTENDANCE_FILE)

# Streamlit UI
st.title("Attendance Management System")

init_file()

menu = ["Mark Attendance", "View Attendance"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Mark Attendance":
    name = st.text_input("Enter Name:")
    if st.button("Mark Attendance"):
        if name:
            mark_attendance(name)
        else:
            st.warning("Please enter a name.")

elif choice == "View Attendance":
    df = load_attendance()
    st.dataframe(df)
    
    if st.button("Download CSV"):
        df.to_csv("attendance_export.csv", index=False)
        st.download_button(label="Download", data=open("attendance_export.csv", "rb"), file_name="attendance.csv", mime="text/csv")
