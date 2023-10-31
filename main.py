import datetime
import time
import sys


for i in range(int(sys.argv[1])):
    time.sleep(1)
    print(datetime.datetime.now())


# створити пайтон файл
# який при запуску отримує аргумент в args - ціле число
# запуск якого щосекунди генерує та друкує час
# протягом кількості секунд, вказаному при запуску програми