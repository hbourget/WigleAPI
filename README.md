# Wigle Location Finder

Ce projet utilise l'API Wigle pour récupérer des données géographiques basées sur un BSSID et/ou un SSID avec en option la possibilité de limité le scope à un pays. En données d'exemple, on requête un SSID en Suisse.

## Fonctionnalités

- Recherche de localisation basée sur :
  - **BSSID** (adresse MAC du point d'accès Wi-Fi, optionel)
  - **SSID** (nom du réseau Wi-Fi, optionel)
  - **Pays** (filtrage par pays, il faut utiliser les codes pays, par exemple FR, CH, BE..., optionel)
- Affichage des coordonnées géographiques (latitude et longitude) des points d'accès trouvés.

## Prérequis

- Python 3.7 ou supérieur
- Une clé API Wigle (inscription sur [wigle.net](https://wigle.net/))

## Lancement
   ```bash
   source .venv/bin/activate
   py main.py --country --ssid --bssid
