from colorama import Fore, Style

cricketers = ["MS Dhoni", "Virat Kohli", "Sachin Tendulkar", "Rohit Sharma"]

print(Fore.CYAN + "My Favorite Cricketers:" + Style.RESET_ALL)
for player in cricketers:
    print(f"- {Fore.YELLOW}{player}{Style.RESET_ALL}")