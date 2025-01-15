# Programa simple para obtener información de una dirección IP

import requests

# Inicio del Sistema

print("\nBienvenido a IP Info Tool! ^^\n")

ip = input("Introduce la direccion IP: ")

if not ip:
    print("Porfavor, Ingrese una direccion IP")
else:
    # Definicion de la API Key y URL

    APIKey = "Introduce tu API Key acá"
    # Introduce tu API Key acá

    url = f"https://ipinfo.io/{ip}/json?token={APIKey}"
    request = requests.get(url)

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

    print("\nGracias por usar IP Info Tool :D")
    print("Hecho por Un Developer Mas/Countryballs El Aleman")
else:
    print("Error al obtener la informacion de la direccion IP, aparecio el codigo {response.status_code}")
    print("Porfavor, Intente de nuevo")

# Hecho por Un Developer Mas/Countryballs El Alemán