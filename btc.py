#!/usr/bin/env python

import json
import os
import sys
from datetime import datetime

import requests

def get_btc_price():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        BTC = data["data"]["amount"]
        btcprice = BTC.split(".")[0]
        return btcprice
    else:
        return None

# Call the function to get the BTC price
btcprice = get_btc_price()

# Check if btcprice is obtained
# if not, Exit
if btcprice is None:
    sys.exit(1)

home_dir = os.environ["HOME"]

data = {}
data["text"] = " BTC $" + btcprice

# print the JSON-formatted data for the waybar
print(json.dumps(data))

filename = home_dir + "/btc_history.txt"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(filename, "a") as file:
    file.write(current_time + " " + btcprice + "\n")
