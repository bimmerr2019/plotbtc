#!/usr/bin/env python
# From https://raw.githubusercontent.com/rxyhn/dotfiles/main/home/rxyhn/modules/desktop/waybar/scripts/waybar-wttr.py

import json
import os
import subprocess
from datetime import datetime

import requests


def runcmd(cmd, verbose=False, *args, **kwargs):

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


home_dir = os.environ["HOME"]
filename = home_dir + "/btc3.json"
runcmd(
    "wget -O " + filename + " -q https://api.coinbase.com/v2/prices/BTC-USD/spot",
    verbose=False,
)

data = {}
# load JSON data from a file
with open(filename, "r") as f:
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
