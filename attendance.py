import firebase_admin
from firebase_admin import credentials, db
import streamlit as st

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://attendance-system-1f6c4-default-rtdb.firebaseio.com/'})

# Fetch attendance data
ref = db.reference("attendance")
data = ref.get()

# Display data in Streamlit Web App
st.title("Real-time Attendance Data")
st.write("Live data from Firebase:")
st.write(data)
