#/usr/bin/python3
import requests
from requests.api import get
from googletrans import Translator
import argparse

translator = Translator()

# Descrizione e aggiunta dell'argomento
parser = argparse.ArgumentParser(description="Dizionario per terminale")
parser.add_argument("frase", type=str, help="Parola da cercare")
args=parser.parse_args()

# Funzione per ottenere il json
def get_json(endpoint):
    response = requests.get(endpoint)
    if response.ok:
        json_data = response.json()
        return json_data
    else:
        print("Status Code: ", response.status_code)

# traduce l'argomento passato da italiano ad inglese (api dizionario in inglese)
toEng = translator.translate(args.frase, src='it', dest='en').text
toEng = toEng.lower()
endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{toEng}"
data = get_json(endpoint)

# Prende la definizione
phrase = data[0]['meanings'][0]['definitions'][0]['definition']
#print(phrase)

# Traduce la definizione in italiano
print(f'Definizione di {args.frase}:', translator.translate(phrase, src='en', dest='it').text)