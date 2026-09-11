import streamlit as st
from Gym_Management import GymMemberManager

member_instance = GymMemberManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Member")
    name = st.text_input("Enter Name")
    place = st.text_input("Enter Place")
    mobile = st.text_input("Enter Mobile Number")
    plan = st.selectbox("Enter Plan",["1month","2month","3month","6month","1year"])
    fee = st.text_input("Enter Fee")
    joined_on = st.text_input("Enter Joining Date(yyyy/mm/dd)")
    if st.button("Submit"):
        member_instance.post(name = name,place = place,mobile = mobile,plan = plan,fee = fee,joined_on=joined_on)
        st.success("New Member Added!")

with tab2:
    st.title("View Members")
    record = member_instance.get()
    if record:
        st.table(record)
    else:
        st.warning("Member Not Found!")