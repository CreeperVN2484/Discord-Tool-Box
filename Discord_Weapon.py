import time
import colorama
from colorama import Fore
import requests
import os
import os.path
from requests.api import options
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Discord Tools v1.0")

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.LIGHTCYAN_EX}Discord Tools \n(Educational and Purposeful attack on Scam Servers only. The creator is not responsible for any misuse of this tool.)
{Fore.RED}
Creator: CreeperVN2484
Version: 1.0

{Fore.YELLOW}Options:
    --------------------------------------------------------------------------------
    | [1] - Server Info Finder       [2] - Exit       [3] - How to find your token?|    
    --------------------------------------------------------------------------------
""")
menu()

try:
 option = int(input(f"{Fore.CYAN} [Input Option >] {Fore.RESET}"))
except ValueError:
 os.system('cls' if os.name == 'nt' else 'clear')
 print("Please enter a valid option")
 print("Exiting in 5 secs...")
 time.sleep(5)
 exit()

def fetch_data():
        menu()
if option == 1:
        time.sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Discord Server Info Finder")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{Fore.GREEN}(Your token (account) must join the server)""")
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n{Fore.LIGHTYELLOW_EX} Authorization Token [>] ")
        }
        

        guildId = input(f"\n{Fore.LIGHTRED_EX} Guild ID. [>] ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""{Fore.LIGHTBLUE_EX}
Name > {response['name']} 
ID > {response['id']}
Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
Approxomate Amount of Members > {response['approximate_member_count']}
Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
Owner ID > {response['owner_id']}
Region > {response['region']}
""")
        time.sleep(10)
        exit()

elif option == 2:
    time.sleep(0.5)
    print(f"{Fore.LIGHTGREEN_EX}Leaving CLI...")
    time.sleep(3)
    exit()

elif option == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.GREEN}Open {Fore.RED}Developer Tools{Fore.GREEN}, then click {Fore.RED}Network{Fore.GREEN}. Press F5 on your keyboard to reload the page. {Fore.RED}Type /api into the Filter field{Fore.GREEN}, then click {Fore.RED}library key name{Fore.GREEN}. Click the {Fore.RED}Headers{Fore.GREEN} tab, then scroll down to {Fore.RED}Request Header > authorization{Fore.GREEN} to find your Discord token. That's it! {Fore.CYAN} (This is for Chrome Browser!)""")
    print("""    
    -------------------------------------
    |[1] - Back to Menu       [2] - Exit|
    -------------------------------------
    """)
    option_2 = int(input(f"{Fore.CYAN} [Input Option >] {Fore.RESET}"))
    if option_2 == 1:
        os.system("py Discord_Weapon.py")
        exit()
    elif option_2 == 2:
        exit()

elif option >= 4:
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Please enter a valid option")
  print("Exiting in 5 secs...")
  time.sleep(5)
  exit()

if __name__ == '__main__':
        fetch_data()
