import streamlit as st
import sqlite3
import pandas as pd

DB_FILE = "attendance.db"

st.title("📸 Face Recognition Attendance System")

# Connect to database
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Ensure the table exists
c.execute('''CREATE TABLE IF NOT EXISTS attendance (name TEXT, time TEXT)''')
conn.commit()

# Fetch data safely
try:
    df = pd.read_sql("SELECT * FROM attendance", conn)
    st.dataframe(df)
except Exception as e:
    st.error(f"⚠️ Error loading attendance data: {e}")

conn.close()
