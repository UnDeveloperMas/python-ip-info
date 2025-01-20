# IP Info Tool, Programa para obtener información de una dirección IP

'''
Acá va la Importación de Librerias, usa pip install para instalar las librerias necesarias, excepto sys, 
ya que es una libreria nativa de Python
'''

import sys
import requests

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# Inicio del Sistema Central

cprint(figlet_format('IP Info Tool', font='starwars'),
       'white', 'on_black', attrs=['bold'])

# Título ASCII decorativo

print("\nBienvenido a IP Info!\n")

ip = input("Introduce la direccion IP: ")

if not ip:
    print("Porfavor, Ingrese una direccion IP")
else:
    # Definicion de la API Key y URL

    APIKey = "Introduce Tu API Key"

    # Introduce tu API Key acá, puedes obtener una en https://ipinfo.io/signup

    url = f"https://ipinfo.io/{ip}/json?token={APIKey}"
    request = requests.get(url)

# Verificación de la respuesta del servidor,  si es exitosa se ejecuta la información de la dirección IP

if request.status_code == 200:
    data = request.json()

    print("\nInformacion de la direccion IP\n")

    print("IP:", data["ip"])
    print("Ciudad:", data["city"])
    print("Region:", data["region"])
    print("Pais:", data["country"])
    print("ISP:", data["org"])
    print("Coordenadas:", data["loc"])
    print("Zona Horaria:", data["timezone"])

    print("\nGracias por usar IP Info")
    print("Hecho por Un Developer Mas/Countryballs El Aleman")
else:
    print("\nError al obtener la informacion de la direccion IP, revise su API Key")
    print("Porfavor, Intente de nuevo")

# Hecho por Un Developer Mas/Countryballs El Alemán
