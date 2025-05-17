import streamlit as st

st.title("Welcome TO Login Page")
st.write("To Reset your Attempt To 3 put admin123")

inp = st.text_input("Enter Login Details")
but = st.button("Enter")

if but:
    if inp == "admin123":
        st.session_state["attempt"] = 3
        st.success("Your attempt Changed To 3")