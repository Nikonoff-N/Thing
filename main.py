from reader import get_active,get_failed,get_all
from scraper import get_info,ProductData
from writer import write_data
import sys
from time import sleep
try:
    timeout = int(sys.argv[1])
except:
    timeout = 0
active = get_all()
data = []
for row in active:
    #print(row)
    link = row[1]
    state = row[2]
    if state == "A" or state == "N":
        pd = get_info(link)
    else:
        pd = ProductData(None,None,None,state)
    data.append(pd)
    if timeout>0:
        print(f"Ждём {timeout//60} минут {timeout%60} секунд до следующего запроса ")
        sleep(timeout)
print(data)
write_data(data)
input("Press Enter to close window")