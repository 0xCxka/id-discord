import requests
import os
import time
import re
from colorama import init, Fore, Style
from tabulate import tabulate


init()


config_file = 'config.txt'
if not os.path.exists(config_file):
    bot_token = input("Enter your Discord bot token: ")
    with open(config_file, 'w') as f:
        f.write(bot_token)
else:
    with open(config_file, 'r') as f:
        bot_token = f.readline().strip()


headers = {
    'Authorization': f'Bot {bot_token}'
}

response = requests.get('https://discord.com/api/users/@me', headers=headers)

while response.status_code != 200:
    print(f'{Fore.RED}Invalid bot token in config file.{Style.RESET_ALL}')
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    bot_token = input("Enter your Discord bot token: ")
    with open(config_file, 'w') as f:
        f.write(bot_token)
    headers = {
        'Authorization': f'Bot {bot_token}'
    }
    response = requests.get('https://discord.com/api/users/@me', headers=headers)


message = "id lookup by @soluce/cxka"
for i in range(len(message)):
    print(message[:i] + Fore.RED + message[i] + Style.RESET_ALL + message[i+1:], end="\r")
    time.sleep(0.1)
print(" " * len(message), end="\r")


print(Fore.RED + "Enter the user ID: " + Style.RESET_ALL, end="")
user_id = input()


while not re.match(r'^\d{17,19}$', user_id):
    print(f'{Fore.RED}Invalid user ID format. Please enter a valid user ID.{Style.RESET_ALL}')
    print(Fore.RED + "Enter the user ID: " + Style.RESET_ALL, end="")
    user_id = input()


os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED + "Loading...\n" + Style.RESET_ALL)
bar_length = 20
for i in range(bar_length + 1):
    bar = "[" + "=" * i + " " * (bar_length - i) + "]"
    percentage = i * 100 // bar_length
    print(f"{Fore.RED}{bar} {percentage}%{Style.RESET_ALL}", end="\r")
    time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')

response = requests.get(f'https://discord.com/api/users/{user_id}', headers=headers)

while response.status_code != 200:
    print(f'{Fore.RED}Error retrieving user information. Status code: {response.status_code}.{Style.RESET_ALL}')
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Enter your Discord bot token: " + Style.RESET_ALL, end="")
    bot_token = input()
    headers = {
        'Authorization': f'Bot {bot_token}'
    }
    response = requests.get(f'https://discord.com/api/users/{user_id}', headers=headers)


with open(config_file, 'w') as f:
    f.write(bot_token)

user = response.json()
tag = f'{user["username"]}#{user["discriminator"]}'
avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{user["avatar"]}.png'

headers = [Fore.CYAN + 'github.com/soluce1337' + Style.RESET_ALL, Fore.CYAN + 'Follow for more' + Style.RESET_ALL]
table = [
    [Fore.GREEN + 'Discord Tag' + Style.RESET_ALL, tag],
    [Fore.GREEN + 'User ID' + Style.RESET_ALL, user_id],
    [Fore.GREEN + 'Avatar URL' + Style.RESET_ALL, avatar_url],
]

print(tabulate(table, headers=headers, tablefmt='plain'))

input("Press Enter to continue...")

os.system('cls' if os.name == 'nt' else 'clear')