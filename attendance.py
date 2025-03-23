import streamlit as st
import sqlite3
import pandas as pd

st.title("📸 Face Recognition Attendance System")

conn = sqlite3.connect("attendance.db")
df = pd.read_sql("SELECT * FROM attendance", conn)
st.dataframe(df)

conn.close()
