import streamlit as st

st.title("📏 Unit Converter App 📐")
st.markdown("### Convert Length, Weight, and Time Instantly!")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time. Let's make conversions easy! 🚀")

category = st.selectbox("Choose a Category 📚", ["Length", "Weight", "Time"])

def convertor(category,unit,value):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Width":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds To Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours To Minutes":
            return value * 60
        elif unit == "Hours To Day":
            return value / 24
        elif unit == "Days To Hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("Select Conversion  🔄", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Width":
    unit = st.selectbox("Select Conversion  🔄", ["Kilograms to Pounds", "Pounds To Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion  🔄", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours To Minutes", "Hours To Day", "Days To Hours"])

value = st.number_input("Enter Value To Convert")

if st.button("Convert Unit  🔄"):
    result = convertor(category,unit,value)
    st.success(f"✅ The converted value is {result}")

