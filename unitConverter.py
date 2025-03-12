import streamlit as st

st.title("Unit Converter")

conversionType = st.selectbox(
    "Select Conversion Type",
    ["Meter to Centimeter", "Centimeter to Meter"]
)

#Simple Functions
def meterToCentimeter(mInput):
    result = mInput * 100
    return result

def centimeterToMeter(cmInput):
    result = cmInput / 100
    return result

value = st.number_input("Enter Value")

if st.button("Convert"):
    if conversionType == "Meter to Centimeter":
         st.write(f"{value} m is {meterToCentimeter(value)} cm.")
    elif conversionType == "Centimeter to Meter":
         st.write(f"{value} cm is {centimeterToMeter(value)} m.")  