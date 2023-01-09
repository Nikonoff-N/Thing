from reader import get_active,get_failed,get_all
from scraper import get_info,ProductData
from writer import write_data
active = get_all()
data = []
for link in active:
    if link:
        pd = get_info(link)
    else:
        pd = ProductData(None,None,None,"B")
    data.append(pd)
print(data)
write_data(data)