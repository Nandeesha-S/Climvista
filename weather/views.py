import pandas as pd
import joblib
from django.http import JsonResponse

# Load the model only once (outside the view)
model = joblib.load("rainfall_model.pkl")

# Define mapping for month name to column index
MONTH_COLS = {
    'January': 'JAN', 'February': 'FEB', 'March': 'MAR',
    'April': 'APR', 'May': 'MAY', 'June': 'JUN',
    'July': 'JUL', 'August': 'AUG', 'September': 'SEP',
    'October': 'OCT', 'November': 'NOV', 'December': 'DEC'
}

def forecast(request):
    district = request.GET.get("district", "Bengaluru Urban")
    date = request.GET.get("date", "2025-08-03")  # default if not passed

    try:
        # Extract month from date
        month_number = int(date.split("-")[1])
        month_name = pd.to_datetime(date).strftime('%B')
        month_col = MONTH_COLS.get(month_name)

        # Prepare input for model
        X = pd.DataFrame([[district]], columns=["SUBDIVISION"])
        prediction = model.predict(X)[0]  # Assuming model returns one value

        return JsonResponse({
            "district": district,
            "date": date,
            "predicted_rainfall_mm": round(prediction, 2)
        })

    except Exception as e:
        return JsonResponse({"error": str(e)})
