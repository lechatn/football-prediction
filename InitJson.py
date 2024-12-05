import requests
import json
import time
import os
from tqdm import tqdm

def updateData():
    api_key = "107f993a0b184b7984e1929678e3d44d"  # Remplace avec ta clé API
    headers = {
        "X-Auth-Token": api_key
    }
    clubs = returnclubs()
    files=os.listdir('./ressources')
    for i in range(0,len(files)):
        os.remove(f"./ressources/{files[i]}")
    
    for club in clubs.items():
        url = f"https://api.football-data.org/v4/teams/{club[1]}/matches"
        try:
            response = requests.get(url, headers=headers)
            # Vérifie si la requête est réussie
            if response.status_code == 200:
                data = response.json()  # Parse la réponse JSON
                with open(f"./ressources/{club[0]}.json", "w") as file:
                    json.dump(data, file, indent=4)  # Écrit les données dans un fichier JSON
                    print(f"Le fichier {club[0]} a été mis à jour")
            else:
                print(f"Erreur : {response.status_code} - {response.reason}")
        except requests.RequestException as e:
            print(f"Erreur lors de la requête : {e}")
        time.sleep(6)

    url = "https://api.football-data.org/v4/competitions/FL1/standings"
    try:
        response = requests.get(url, headers=headers)
        # Vérifie si la requête est réussie
        if response.status_code == 200:
            data = response.json()  # Parse la réponse JSON
            with open(f"./ressources/standings.json", "w") as file:
                json.dump(data, file, indent=4)  # Écrit les données dans un fichier JSON
                print("Le fichier standings a été mis à jour")
        else:
            print(f"Erreur : {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

def returnclubs():
    clubs = {
        "Toulouse FC": "511",
        "Stade Brestois 29": "512",
        "Olympique de Marseille": "516",
        "Montpellier HSC": "518",
        "AJ Auxerre": "519",
        "Lille OSC": "521",
        "OGC Nice": "522",
        "Olympique Lyonnais": "523",
        "Paris Saint-Germain FC": "524",
        "AS Saint-Étienne": "527",
        "Stade Rennais FC 1901": "529",
        "Angers SCO": "532",
        "Le Havre AC": "533",
        "FC Nantes": "543",
        "Racing Club de Lens": "546",
        "Stade de Reims": "547",
        "AS Monaco FC": "548",
        "RC Strasbourg Alsace": "576",
    }
    return clubs
    
