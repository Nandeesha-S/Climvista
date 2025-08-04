import streamlit as st
import requests
import os

# You can optionally load .env if using one
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY") or "fb9eeacc2e66f6961e235d577dbc98fb"  # fallback API key

district_to_city = {
    "Bagalkote": "Bagalkot",
    "Ballari": "Bellary",
    "Belagavi": "Belgaum",
    "Bengaluru Rural": "Bengaluru",
    "Bengaluru Urban": "Bengaluru",
    "Bidar": "Bidar",
    "Chamarajanagara": "Chamarajanagar",
    "Chikkaballapur": "Chikkaballapur",
    "Chikkamagaluru": "Chikmagalur",
    "Chitradurga": "Chitradurga",
    "Dakshina Kannada": "Mangalore",
    "Davanagere": "Davanagere",
    "Dharwad": "Dharwad",
    "Gadag": "Gadag",
    "Hassan": "Hassan",
    "Haveri": "Haveri",
    "Kalaburagi": "Gulbarga",
    "Kodagu": "Madikeri",
    "Kolar": "Kolar",
    "Koppal": "Koppal",
    "Mandya": "Mandya",
    "Mysuru": "Mysore",
    "Raichur": "Raichur",
    "Ramanagara": "Ramanagara",
    "Shivamogga": "Shimoga",
    "Tumakuru": "Tumkur",
    "Udupi": "Udupi",
    "Uttara Kannada": "Karwar",
    "Vijayapura": "Bijapur",
    "Vijayanagara": "Hospet",
    "Yadgir": "Yadgir"
}

st.set_page_config(page_title="ClimVista - Karnataka Weather", layout="centered")
st.title("🌤️ ClimVista - Karnataka Weather Dashboard")

# Dropdown for districts
districts = list(district_to_city.keys())
selected_district = st.selectbox("Select a District", districts)

if st.button("Get Weather"):
    city_name = district_to_city.get(selected_district)
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {selected_district}")
        st.metric("🌡 Temperature", f"{data['main']['temp']:.2f}°C")
        st.text(f"🌥 Condition: {data['weather'][0]['description'].title()}")
        icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        st.image(icon_url)
    else:
        st.error("Failed to fetch weather data. Please try again.")
