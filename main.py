import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_URL = os.getenv("NUTRITIONIX_URL")
SHEETY_API_URL = os.getenv("SHEETY_API_URL")
TOKEN = os.getenv("TOKEN")

exercises = input("Tell me what exercises you did: ")

my_params = {
    'query': exercises,
    'gender': 'male',
    'weight_kg': '95.708',
    'height_cm': '177.8',
    'age': 36
}

headers = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_API_KEY}

nutritionix_response = requests.post(url=NUTRITIONIX_URL, json=my_params, headers=headers)
nutritionix_data = nutritionix_response.json()['exercises']

date = dt.datetime.now().strftime('%m/%d/%Y')
time = dt.datetime.now().strftime('%H:%M:%S')

for exercise in nutritionix_data:
    sheety_body = {
        "workout": {
            'date': date,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    headers = {"Authorization": f'Bearer {TOKEN}'}

    sheety_response = requests.post(url=SHEETY_API_URL, json=sheety_body, headers=headers)
    sheety_data = sheety_response.json()


