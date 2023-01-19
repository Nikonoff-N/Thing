import logging
import datetime
from bs4 import BeautifulSoup
import requests


class scrap_error(Exception):
    #logging.error("Failed to get data?whoops")
    pass


class ProductData(object):
    def __init__(self,name:str,price:float,count:int,state:str) -> None:
        self.name = name
        self.price = price
        self.count = count
        self.state=state


def get_info(url:str)->ProductData:
    """Gets CHIPDIP data from URL
    Args:
        url (str): url of product
    Returns:
        tuple: current price,count and name
    """
    r = requests.get(url)
    print(f"{url}-{r.status_code}")
    if r.status_code == 404:
        return ProductData(None,None,None,"B")
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        price = soup.find_all("span", {"class":'ordering__value'})[0]
        count = soup.find_all("span", {"class":'item__avail'})[0]
        name = soup.find("h1", itemprop='name')
    except:
        raise scrap_error(Exception)
    else:
        name = name.text.replace(",",".")
        count_transformed = ""
        for c in count.text.split()[0]:
            if c in "0123456789":
                count_transformed+=c
        if(count_transformed):
            count_transformed = float(count_transformed)
        else:
            count_transformed=0

        price_transformed = ""
        for c in price.text:
            if c in "0123456789":
                price_transformed+=c
        #print(price_transformed)
        price = float(price_transformed)
        data = ProductData(name,count_transformed,price_transformed,"A")
        return data
