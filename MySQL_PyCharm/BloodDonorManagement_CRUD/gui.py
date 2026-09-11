import streamlit as st
from BloodDonorManagement_CRUD import BloodDonorManager

donor_instance = BloodDonorManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Donor")
    name = st.text_input("Enter Blood Donor Name")
    blood_group = st.selectbox("Enter Blood Group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    phone = st.text_input("Enter Phone Number")
    city = st.text_input("Enter City")
    last_donation = st.text_input("Enter Last Donation Date(yyyy/mm/dd)")
    if st.button("Add New Donor"):
        donor_instance.post(name= name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor Added Successfully!")

with tab2:
    st.title("View Donor Details")
    record = donor_instance.get()
    if record:
        st.table(record)
    else:
        st.warning("Donor Not Found!")