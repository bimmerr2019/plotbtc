# plotbtc

These programs grab the btc price every 5 minutes from coinbase and put it in the Hyprland waybar. Each 5 min price is also stored in a btc_history.txt file. The program plotbtc will plot it to your terminal. i like to alias it to "p"

if desired add to .zshrc:

alias p="~/plotbtc/plotbtc"

You will need to edit your .config/waybar/config file and follow the instructions in the add_to_waybar_config file. The waybar module in the config file calls the btc.py program every 5 minutes. Two files will store the btc price in your home directory:

- btc.json
- btc_history.txt

- git clone https://github.com/plotbtc/plotbtc.git
- modify ~/.config/waybar/config

done.
