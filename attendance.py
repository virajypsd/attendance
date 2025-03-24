import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
import datetime
import io

# Firebase setup
cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com/'
})

def fetch_attendance():
    ref = db.reference("attendance")
    data = ref.get()
    if data:
        return pd.DataFrame(data).T
    return pd.DataFrame(columns=["student_name", "lecture", "date", "time", "status"])

# Streamlit UI
st.title("College Attendance Management System")
role = st.selectbox("Select Role", ["Student", "Admin"])

data = fetch_attendance()

date_filter = st.date_input("Filter by Date", datetime.date.today())
lecture_filter = st.text_input("Filter by Lecture")
student_filter = st.text_input("Filter by Student Name")

if not data.empty:
    data['date'] = pd.to_datetime(data['date']).dt.date
    filtered_data = data[(data['date'] == date_filter)]
    
    if lecture_filter:
        filtered_data = filtered_data[filtered_data['lecture'].str.contains(lecture_filter, case=False)]
    if student_filter:
        filtered_data = filtered_data[filtered_data['student_name'].str.contains(student_filter, case=False)]
    
    st.dataframe(filtered_data)
    
    # Export options
    export_format = st.radio("Export Data As", ["CSV", "Excel", "PDF"])
    
    if st.button("Download Data"):
        if export_format == "CSV":
            csv = filtered_data.to_csv(index=False).encode()
            st.download_button("Download CSV", csv, "attendance.csv", "text/csv")
        elif export_format == "Excel":
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                filtered_data.to_excel(writer, index=False, sheet_name='Attendance')
            st.download_button("Download Excel", output.getvalue(), "attendance.xlsx")
        elif export_format == "PDF":
            st.warning("PDF export not yet implemented.")
else:
    st.warning("No attendance records found.")
