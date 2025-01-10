import requests

WIGLE_API_KEY = ""

def get_location(bssid=None, country=None, ssid=None):
    """
    Contacte l'API de Wigle pour récupérer les données géographiques d'un BSSID.

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


if __name__ == "__main__":
    location_data = get_location("5C:DC:96:94:EE:80", "CH")

    if location_data:
        for entry in location_data:
            print(f"SSID: {entry.get('ssid', 'N/A')}")
            print(f"Latitude: {entry.get('trilat')}")
            print(f"Longitude: {entry.get('trilong')}")
            print(f"Pays: {entry.get('country')}")
    else:
        print("Aucune donnée trouvée pour ces paramètres.")
