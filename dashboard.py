import streamlit as st
import pandas as pd

st.title("Attendance App for VGU")
st.text("Welcome to our dashboard")


if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = pd.DataFrame(columns=["Name", "Subject", "Status"])


name = st.text_input("Enter your name:")
subject = st.text_input("Subject:")
attendance = st.selectbox("Enter your attendance:", ["Present", "Absent"])

if st.button("Submit Attendance"):
    if name and subject:
        new_row = {"Name": name, "Subject": subject, "Status": attendance}
        st.session_state.attendance_data = st.session_state.attendance_data._append(new_row, ignore_index=True)
        st.success(f"Attendance Submitted for {name}!")
    else:
        st.error("Please fill all details!")

st.write(" All Attendance Records")
st.dataframe(st.session_state.attendance_data)


st.write(" Student-wise Attendance Chart")

if name.strip() != "":
 
    student_data = st.session_state.attendance_data[st.session_state.attendance_data["Name"] == name]

    if not student_data.empty:
        chart_data = student_data["Status"].value_counts()
        st.bar_chart(chart_data)
    else:
        st.info(f"No attendance data found for **{name}**")
else:
    st.info("Enter a name to view attendance chart.")
