import streamlit as st
from EmployeeManagement import EmployeeManager

employee_instance = EmployeeManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Employee")
    # name, place, mobile, email, department, salary, joining_date
    name = st.text_input("Enter Name")
    place = st.text_input("Enter Place")
    mobile = st.text_input("Enter Mobile")
    email = st.text_input("Enter Email")
    department = st.text_input("Enter Department")
    salary = st.text_input("Enter salary")
    joining_date = st.text_input("Enter Joining Date(yyyy/mm/dd)")
    if st.button("Submit"):
        employee_instance.post(name = name,place = place,mobile= mobile,email = email,department = department,salary= salary,joining_date= joining_date)
        st.success("Employee Added Successfully!")

with tab2:
    st.title("View Employees")
    record = employee_instance.get()
    if record:
        st.table(record)
    else:
        st.warning("Employee Not Found!")
