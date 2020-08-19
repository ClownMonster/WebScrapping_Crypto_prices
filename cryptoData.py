#imports for scrapping

from bs4 import BeautifulSoup
import requests
import json


response = requests.get("https://coinmarketcap.com/") # url request fetch

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    data  =  soup.find('script', id = "__NEXT_DATA__", type = "application/json")
    coins = {}

    coin_data = json.loads(data.contents[0])
    coins_list = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

    # getting the entire crypto data
    print(coins_list)


else:
    print("Unable to Fetch the Data")