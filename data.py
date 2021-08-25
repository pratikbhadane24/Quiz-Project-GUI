from question_model import Question
import requests

paramerters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=paramerters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
