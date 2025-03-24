import streamlit as st
import pandas as pd
import datetime
import io

# Sample Data
data = pd.DataFrame({
    "student_name": ["Alice", "Bob", "Charlie", "David"],
    "lecture": ["Math", "Science", "History", "English"],
    "date": ["2025-03-24", "2025-03-24", "2025-03-23", "2025-03-23"],
    "time": ["10:00 AM", "11:00 AM", "09:00 AM", "12:00 PM"],
    "status": ["Present", "Late", "Absent", "Present"]
})

data['date'] = pd.to_datetime(data['date']).dt.date

# Streamlit UI
st.title("College Attendance Management System")
role = st.selectbox("Select Role", ["Student", "Admin"])

date_filter = st.date_input("Filter by Date", datetime.date.today())
lecture_filter = st.text_input("Filter by Lecture")
student_filter = st.text_input("Filter by Student Name")

filtered_data = data[data['date'] == date_filter]
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
