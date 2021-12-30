#/usr/bin/python3
from googletrans import Translator
import argparse

translator = Translator()

parser = argparse.ArgumentParser(description="Translator for bash terminal")

parser.add_argument("lang_src", type=str, help="Source Language")
parser.add_argument("lang_dest", type=str, help="Destination Language")
parser.add_argument("phrase", type=str, help="Phrase to translate")
args=parser.parse_args()

transPhrase = translator.translate(args.phrase, src=args.lang_src, dest=args.lang_dest).text

if(transPhrase.lower() != args.phrase.lower()):
    print(f"Translation of '{args.phrase}': {transPhrase}")
else:
    print("Parola non riconosciuta")



