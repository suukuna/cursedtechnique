import requests
import time

base_url = 'http://api.open-notify.org/iss-now.json'


while True:
    time.sleep(5)
    with open('data.csv', 'a') as file:
        response = requests.get(base_url)
        data = response.json()
        result = f'{data["iss_position"]["longitude"]};{data["iss_position"]["latitude"]}\n'
        file.write(result)
        print(data)
        print(result)
