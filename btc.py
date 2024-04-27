#!/usr/bin/env python
# From https://raw.githubusercontent.com/rxyhn/dotfiles/main/home/rxyhn/modules/desktop/waybar/scripts/waybar-wttr.py

import json
import os
from datetime import datetime

import requests

data = {}
home_dir = os.environ["HOME"]
# load JSON data from a file
with open(home_dir + "/btc.json", "r") as f:
    data1 = json.load(f)

# parse the JSON data
BTC = data1["data"]["amount"]
btcprice = BTC.split(".")[0]
data["text"] = " BTC $" + btcprice

# print the JSON-formatted data
print(json.dumps(data))

filename = home_dir + "/btc_history.txt"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(filename, "a") as file:
    file.write(current_time + " " + btcprice + "\n")
