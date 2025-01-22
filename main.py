 import os

import requests
import argparse
import folium

WIGLE_API_KEY = os.getenv("WIGLE_API_KEY")

def get_location(bssid=None, country=None, ssid=None):
    """
    Utilise l'API de Wigle pour récupérer les données géographiques d'un BSSID.

    :param bssid: Le BSSID (adresse MAC) du point d'accès Wi-Fi (optionnel)
    :param country: Le pays dans lequel chercher (optionnel)
    :param ssid: Le SSID du point d'accès Wi-Fi (optionnel)
    :return: Les données sous forme de dict
    """
    url = "https://api.wigle.net/api/v2/network/search"
    headers = {"Authorization": f"Basic {WIGLE_API_KEY}"}
    params = {}

    if bssid:
        params["netid"] = bssid
    if ssid:
        params["ssid"] = ssid
    if country:
        params["country"] = country

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if "success" in data and data["success"] is True:
            return data.get("results", [])
        else:
            print("Erreur dans la réponse API:", data.get("message"))
            return None
    else:
        print(f"Erreur HTTP {response.status_code}: {response.text}")
        return None

def create_map(latmap, lonmap, ssidmap):
    """
    Crée une carte interactive avec un marqueur à l'emplacement spécifié avec folium.

    :param latmap: Latitude
    :param lonmap: Longitude
    :param ssidmap: Nom du réseau Wi-Fi
    """
    map_ = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker(
        [latmap, lonmap],
        popup=f"SSID: {ssidmap}",
        tooltip="Cliquez pour plus d'infos"
    ).add_to(map_)
    map_.save("map.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bssid", help="Le BSSID (adresse MAC) du point d'accès Wi-Fi", required=False)
    parser.add_argument("--country", help="Le pays dans lequel chercher", required=False)
    parser.add_argument("--ssid", help="Le SSID du point d'accès Wi-Fi", required=False)

    args = parser.parse_args()

    if not any([args.bssid, args.country, args.ssid]):
        print("Aucun argument fourni. Utilisez --bssid, --country ou --ssid pour rechercher des données.")
    else:
        location_data = get_location(bssid=args.bssid, country=args.country, ssid=args.ssid)

        if location_data:
            for entry in location_data:
                ssid = entry.get("ssid", "N/A")
                lat = entry.get("trilat")
                lon = entry.get("trilong")
                country = entry.get("country")
                encryption = entry.get("encryption")

                print(f"SSID: {ssid}")
                print(f"Latitude: {lat}")
                print(f"Longitude: {lon}")
                print(f"Pays: {country}")
                print(f"Chiffrement: {encryption}")

                create_map(lat, lon, ssid)
        else:
            print("Aucune donnée trouvée pour ces paramètres.")
