"""A Streamlit application for unit conversion with a custom styled interface."""

import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: purple;
        color: pink;
    }
    .stApp {
        background: linear-gradient(135deg,rgb(177, 20, 169),rgb(182, 150, 212));
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(130, 26, 156, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg,rgb(90, 7, 86),rgb(125, 55, 172));
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(190, 11, 146, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg,rgb(226, 65, 145), rgb(247, 189, 218));
        text: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(218, 43, 151, 0);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(135, 7, 219, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and descrition
st.markdown("<h1> Unit convertor using python and streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between differen units of length, weight, and temperature.")

#side menu
conversion_type = st.sidebar.selectbox(
    "Choose the conversion type", 
    ["Length", "Weight", "Temperature"]
)
value = st.sidebar.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox(
            "From", 
            ["Meters", "Centimeters", "Millimeters", "Kilometers", "Miles", "Feet", "Yards", "Inches"]
        )
    with col2:
        to_unit = st.selectbox(
            "To", 
            ["Meters", "Centimeters", "Millimeters", "Kilometers", "Miles", "Feet", "Yards", "Inches"]
        )
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converted functions
def convert_length(value, from_unit, to_unit):
    """Convert length between different units."""
    length_conversion = {
        "Meters": 1.0,
        "Centimeters": 100.0,
        "Millimeters": 1000.0,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Inches": 39.3701
    }
    if from_unit == to_unit:
        return value
    return (value / length_conversion[from_unit] * length_conversion[to_unit])

def convert_weight(value, from_unit, to_unit):
    """Convert weight between different units."""
    weight_conversion = {
        "Kilograms": 1.0,
        "Grams": 1000.0,
        "Milligrams": 1000000.0,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    if from_unit == to_unit:
        return value
    return (value / weight_conversion[from_unit] * weight_conversion[to_unit])

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between different units."""
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

#button and conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Unit Convertor by Dilkash Maryam🌸</div>", unsafe_allow_html=True)