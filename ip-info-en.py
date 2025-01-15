# Simple program to get info about an IP address

import requests

# Start of the System

print("\nWelcome to IP Info Tool! ^^\n")

ip = input("Enter an IP address: ")

if not ip:
    print("Please, Enter an IP address")
else:
    # Defining the API Key and URL

    APIKey = "Put your API Key here"
    # Put your API Key here

    url = f"https://ipinfo.io/{ip}/json?token={APIKey}"
    request = requests.get(url)

if request.status_code == 200:
    data = request.json()

    print("\nInformation of the IP address\n")

    print("IP:", data["ip"])
    print("City:", data["city"])
    print("Region:", data["region"])
    print("Country:", data["country"])
    print("ISP:", data["org"])
    print("Coordinates:", data["loc"])
    print("Timezone:", data["timezone"])

    print("\nThanks for using IP Info Tool :D")
    print("Made by Un Developer Mas/Countryballs El Aleman")
else:
    print("Got an error while trying to get IP's info, got code {response.status_code}")
    print("Please, try again")

# Made by Un Developer Mas/Countryballs El Alemán