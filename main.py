import datetime
import time
import sys


for i in range(int(sys.argv[1])):
    time.sleep(1)
    print(datetime.datetime.now())
