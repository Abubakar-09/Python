import streamlit as st

st.title("Unit Coversion Promax")

category = st.selectbox("Choose Category", ["Lenght","Time"])

def Lenght_conversion(con_type,con_units):
    if con_type == "Km":
        return con_units*1000
    elif con_type == "Mile":
        return con_units*1609.34    

def Time_conversion(con_type,con_units):            
    if con_type == "Hour":
        return con_units*60*60
    elif con_type == "Day":
        return con_units*24*60*60

if category == "Lenght":
    from_unit = st.selectbox("From to Meter", ["Km", "Mile"])
    units = st.number_input("Enter a Number")
    if from_unit == "Km":
        total = Lenght_conversion("Km",units)
        st.write(f"Converted into {total} meters.")
    elif from_unit == "Mile":
        total = Lenght_conversion("Mile",units)
        st.write(f"Converted into {total} meters.")        
elif category == "Time": 
    from_unit = st.selectbox("From to Sec", ["Hour", "Day"])
    units = st.number_input("Enter a Number")
    if from_unit == "Hour":
        total = Time_conversion("Hour",units)
        st.write(f"Converted into {total} Sec.")
    elif from_unit == "Day":
        total = Time_conversion("Day",units)
        st.write(f"Converted into {total} Sec.")