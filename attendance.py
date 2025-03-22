import streamlit as st
import pandas as pd
import os

# Attendance data file
ATTENDANCE_FILE = "attendance.csv"

# Load attendance data
def load_data():
    if os.path.exists(ATTENDANCE_FILE):
        return pd.read_csv(ATTENDANCE_FILE)
    return pd.DataFrame(columns=["Name", "Date", "Time", "Subject"])

# Save new attendance data
def save_data(df):
    df.to_csv(ATTENDANCE_FILE, index=False)

# UI Layout
st.title("📚 Face Recognition Attendance System")
st.sidebar.header("Filter Options")

# Load data
df = load_data()

# Get unique subjects
subjects = df["Subject"].unique().tolist()
subjects.sort()

# Subject filter
subject_filter = st.sidebar.selectbox("Select Subject", ["All"] + subjects)

# Date filter
date_filter = st.sidebar.date_input("Select Date", None)
if date_filter:
    df = df[df["Date"] == date_filter.strftime("%Y-%m-%d")]

# Name filter
name_filter = st.sidebar.text_input("Search by Name").strip().lower()
if name_filter:
    df = df[df["Name"].str.lower().str.contains(name_filter, na=False)]

# Apply subject filter
if subject_filter != "All":
    df = df[df["Subject"] == subject_filter]

# Display Data
st.subheader(f"Attendance Records ({subject_filter})")
st.write(df)

# Attendance Summary
st.subheader("Summary")
total_entries = len(df)
unique_names = df["Name"].nunique()
st.write(f"✅ Total Entries: {total_entries}")
st.write(f"👥 Unique Students: {unique_names}")

# Export Filtered Data
if st.button("Download CSV"):
    df.to_csv("filtered_attendance.csv", index=False)
    st.success("File saved as filtered_attendance.csv")

# Auto-refresh
st.experimental_rerun()

