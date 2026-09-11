import streamlit as st
from Student_CRUD import Student

student_instance = Student()
tab1 , tab2 = st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Student")
    # id, name, age, place
    id = st.text_input("Enter Id")
    name = st.text_input("Enter Name")
    age = st.text_input("Enter Age")
    place = st.text_input("Enter Place")
    if st.button("Submit"):
        student_instance.post(id= id,name= name,age= age,place = place)
        st.success("Student Added!")
with tab2:
    st.title("View Students")
    record = student_instance.get()
    if record:
        st.table(record)
    else:
        st.warning("Student Not Found!")