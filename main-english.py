# IP Info Tool, Program to obtain information from an IP address

'''
Here goes the Library Import, use pip install to install the necessary libraries, except sys, 
since it is a native Python library.
'''

import sys
import requests

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# Start of the Central System

cprint(figlet_format('IP Info Tool', font='starwars'),
       'white', 'on_black', attrs=['bold'])

# Decorative ASCII Title

print("\nWelcome to IP Info!\n")

ip = input("Enter the IP address: ")

if not ip:
    print("Please, enter an IP address")
else:
    # Define the API Key and URL

    APIKey = "Enter your API Key"

    # Enter your API Key here, you can get one at https://ipinfo.io/signup

    url = f"https://ipinfo.io/{ip}/json?token={APIKey}"
    request = requests.get(url)

# Server response verification, if successful the IP address information is shown

if request.status_code == 200:
    data = request.json()

    print("\nIP address information\n")

    print("IP:", data["ip"])
    print("City:", data["city"])
    print("Region:", data["region"])
    print("Country:", data["country"])
    print("ISP:", data["org"])
    print("Coordinates:", data["loc"])
    print("Time Zone:", data["timezone"])

    print("\nThank you for using IP Info")
    print("Made by Un Developer Mas/Countryballs The German")
else:
    print("\nError getting the IP address information, check your API Key")
    print("Please, try again")

# Made by Un Developer Mas/Countryballs The German
