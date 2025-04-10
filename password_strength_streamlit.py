import re # for searching and manipulating the strings in pyhton
import string 
import random
import streamlit as st

st.title("PassWord Generator / Checker Pro Max")

password = st.text_input("Enter Your Password")
enter_but = st.button("Submit / check")

def check_pass(user_inputs:str):
    feedback = []
    score = 0
    suggestion = ''

    # for digits 
    if (re.search(r"\d", user_inputs)):
        score += 1
    else:
        feedback.append({"but":"warning", "message":"No Digits In it, Please Put Atleast One"})

    # for small alphabets 
    if (re.search(r"[a-z]", user_inputs)):
        score += 1
    else:
        feedback.append({"but":"warning", "message":"No Small Alphabet In it, Please Put Atleast One"})

    # for large alpha... 
    if (re.search(r"[A-Z]", user_inputs)):
        score += 1
    else:
        feedback.append({"but":"warning", "message":"No Large Alphabet In it, Please Put Atleast One"})

    # for special character 
    if (re.search(r"[!@£$%^&*]", user_inputs)):
        score += 1
    else:
        feedback.append({"but":"warning", "message":"No Special Character In it, Please Put Atleast One"})  

    # for lenght 
    if (len(user_inputs) > 7 ):
        score += 1
    else:
        feedback.append({"but":"warning", "message":"Less than 8 character please put more than 7 characters."}) 

    # now to run the feedbacks 
    for i in feedback:
        if i["but"] == "warning":
            st.warning(f"{i["message"]}")  

    if score>=0 and score <=2:
        st.error("Your Password Scored low: Weak Password")
    elif score>=3 and score <=4:
        st.info("Your Password Scored Mid: Good Password")
    elif score == 5:
        st.success("Your Password Scored High: Excellent Password") 

    # func for random pass 
    def ran_pass():
        can_contain = string.ascii_letters + string.digits + string.punctuation
        ran_pass = ''
        for i in range(13):
            ran_pass += random.choice(can_contain)
        return ran_pass

    # put in suggestion 
    suggestion = ran_pass()
    st.write(f"A Random Unique and good Password You can Take : {suggestion}")                       


if enter_but:
    check_pass(password)