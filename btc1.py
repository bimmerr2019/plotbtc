#!/usr/bin/env python

import json
import os
import shutil
import sys
import time
from datetime import datetime

import requests


def get_btc_price():
    try:
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            BTC = data["data"]["amount"]
            btcprice = BTC.split(".")[0]
            return btcprice
        else:
            return None
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching price: {e}", file=sys.stderr)
        return None


def create_block_text(text):
    # Bigger block letters using Unicode block characters (4x7 instead of 3x5)
    block_chars = {
        "0": ["████", "█  █", "█  █", "█  █", "█  █", "█  █", "████"],
        "1": [" ██ ", "███ ", " ██ ", " ██ ", " ██ ", " ██ ", "████"],
        "2": ["████", "   █", "   █", "████", "█   ", "█   ", "████"],
        "3": ["████", "   █", "   █", "████", "   █", "   █", "████"],
        "4": ["█  █", "█  █", "█  █", "████", "   █", "   █", "   █"],
        "5": ["████", "█   ", "█   ", "████", "   █", "   █", "████"],
        "6": ["████", "█   ", "█   ", "████", "█  █", "█  █", "████"],
        "7": ["████", "   █", "   █", "   █", "   █", "   █", "   █"],
        "8": ["████", "█  █", "█  █", "████", "█  █", "█  █", "████"],
        "9": ["████", "█  █", "█  █", "████", "   █", "   █", "████"],
        "B": ["███ ", "█  █", "█  █", "███ ", "█  █", "█  █", "███ "],
        "T": ["████", " ██ ", " ██ ", " ██ ", " ██ ", " ██ ", " ██ "],
        "C": ["████", "█   ", "█   ", "█   ", "█   ", "█   ", "████"],
        "$": [" ██ ", "████", "█   ", "████", "   █", "████", " ██ "],
        " ": ["    ", "    ", "    ", "    ", "    ", "    ", "    "],
        "E": ["████", "█   ", "█   ", "███ ", "█   ", "█   ", "████"],
        "R": ["███ ", "█  █", "█  █", "███ ", "█ █ ", "█  █", "█  █"],
        "O": ["████", "█  █", "█  █", "█  █", "█  █", "█  █", "████"],
    }

    lines = ["", "", "", "", "", "", ""]
    for char in text.upper():
        if char in block_chars:
            for i in range(7):
                lines[i] += block_chars[char][i] + "  "  # Extra space between chars
        else:
            for i in range(7):
                lines[i] += "      "

    return lines


def center_text(lines, timestamp_line=""):
    # Get terminal dimensions
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns
    terminal_height = terminal_size.lines

    # Find the longest line to calculate horizontal padding
    max_length = max(len(line) for line in lines)
    if timestamp_line:
        max_length = max(max_length, len(timestamp_line))

    # Calculate horizontal padding for centering
    h_padding = max(0, (terminal_width - max_length) // 2)

    # Add horizontal padding to each line
    centered_lines = [" " * h_padding + line for line in lines]

    # Add timestamp if provided
    if timestamp_line:
        centered_lines.append(" " * h_padding + timestamp_line)

    # Calculate vertical padding for centering
    content_height = len(centered_lines)
    v_padding = max(0, (terminal_height - content_height) // 2)

    # Add vertical padding
    output = "\n" * v_padding + "\n".join(centered_lines)

    return output


def clear_screen():
    os.system("clear")


def display_btc_price():
    clear_screen()

    btcprice = get_btc_price()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if btcprice is None:
        # Display error message in block text
        text = "ERROR"
        block_lines = create_block_text(text)
        error_msg = "Failed to fetch BTC price. Retrying in 60 seconds..."
        centered_output = center_text(
            block_lines, f"Last updated: {timestamp} - {error_msg}"
        )
        print(centered_output, flush=True)
        return False

    text = f"BTC ${btcprice}"
    block_lines = create_block_text(text)
    centered_output = center_text(block_lines)

    print(centered_output, flush=True)
    return True


def main():
    try:
        while True:
            display_btc_price()
            # Wait for 60 seconds before next update
            time.sleep(60)
    except KeyboardInterrupt:
        clear_screen()
        print("BTC Price monitor stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
