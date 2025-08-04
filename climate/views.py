import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")


# ✅ Map 31 districts to OpenWeatherMap-compatible city names
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

districts = list(district_to_city.keys())

def forecast(request):
    result = None
    selected_district = None

    if request.method == "POST":
        selected_district = request.POST.get("district")
        city_name = district_to_city.get(selected_district)

        api_key = "fb9eeacc2e66f6961e235d577dbc98fb"  # Replace with your key!
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            result = {
                "district": selected_district,
                "temperature": f"{data['main']['temp']:.2f}°C",
                "condition": data['weather'][0]['description'].title(),
                "icon": data['weather'][0]['icon']
            }
        else:
            result = {
                "district": selected_district,
                "temperature": "N/A",
                "condition": "City Not Found",
                "icon": None
            }

    return render(request, "climate/forecast.html", {
        "districts": districts,
        "result": result
    })
