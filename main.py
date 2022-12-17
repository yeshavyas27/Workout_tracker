import requests
from datetime import datetime

APP_ID = "41875b59"
API_KEY = "9d9db3dd2000b2ea364d639efa38bf84"
sheety_auth = "Basic eWVzaGF2eWFzMjc6WWVzaGFAMTIz"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0124e3c397cd0ed21fa49c1eeb9c3f28/workoutProject/workouts"

message_input = input("How much exercise did you do today? ")

exercise_headers= {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": message_input,
    "gender": "F",
     "weight_kg": 50,
     "height_cm": 153.924,
     "age": 19
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
result = response.json()
exercises = result["exercises"]

today = datetime.now()
date = today.date().strftime("%d/%m/%Y")
time = today.time().strftime("%H:%M:%S")

for exercise in exercises:
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    name_exercise = exercise["name"]

    add_data = {
        "workout":
            {
                "date": date,
                "time": time,
                "exercise": name_exercise.title(),
                "duration": duration,
                "calories": calories
            }
    }
    sheety_header = {
        "Authorization": sheety_auth,
        "Content-Type": "application/json"
    }

    response_sheet = requests.post(url=sheet_endpoint, json=add_data, headers=sheety_header)
    print(response_sheet.text)
