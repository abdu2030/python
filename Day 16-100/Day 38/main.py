import requests

APP_ID =  "app_99a12388c99e4d56a6454e2f"
API_KEY ="nix_live_jZ1a3WzBRWPRb1MkJyOQDVAW7Y5kbmQC"



GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 170
AGE = 22



exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)