import requests
import time

base_url = 'http://api.open-notify.org/iss-now.json'


while True:
    time.sleep(5)
    with open('data.csv', 'a') as file:
        response = requests.get(base_url)
        data = response.json()
        result = f'{data["iss_position"]["longitude"]};{data["iss_position"]["latitude"]}'
        file.write(result)
        print(data)
        print(result)


# написати програму, яка кожні 5 секунд записує  в csv файл
#
#  (нагадую, це текстовий файл, в якому значення умовних колонок розділяються крапкою та комою (;) )
#
# дані про положення Міжнародної космічної станції по довжині та широті
#
# посилання тут http://api.open-notify.org/iss-now.json
#
# на основі даної програми створити докорфайл, код завантажити в докер імедж, та запустити в контейнері
#
# здати код проєкту на гіті