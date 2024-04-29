# plotbtc

These programs grab the btc price every 5 minutes from coinbase and put it in the Hyprland waybar. Each 5 min price is also stored in a btc_history.txt file. The program plotbtc will plot it to your terminal. i like to alias it to "p"

if desired add to .zshrc:

alias p="~/plotbtc/plotbtc"

You will need to edit your .config/waybar/config file and follow the instructions in the add_to_waybar_config file. The waybar module in the config file calls the btc.py program every 5 minutes. The btc price history is stored in your home directory:

- btc_history.txt

So the install is:

- cd
- git clone https://github.com/plotbtc/plotbtc.git
- modify ~/.config/waybar/config

You will need to refresh your waybar:

- refresh waybar (mine is super ALT r, but yours will be different)
