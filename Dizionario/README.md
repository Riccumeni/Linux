
# Dizionario italiano
## Introduzione
Questa è una guida per installare e usare questo dizionario italiano per terminale linux bash.
***
## Installazione
1. Installare la libreria di google trans con: (installare pip se non è ancora installato!) <br>
`pip install googletrans==4.0.0-rc1` 
2. Installare la libreria di requests con : <br>
`pip install requests`
3. Spostare il programma nella cartella /bin con il comando `cp`
4. Aggiungere nel file .bashrc situato nella cartella home la seguente riga: <br>
`alias dizionario="python3 /bin/dizionario.py"`
***
## Utilizzo

Inserire la keyword dizionario + la parola.

Esempio: <br>
`$ dizionario ciao` <br>
Il cui risultato sarà: <br>
`Definizione di ciao: usato come un saluto o per iniziare una conversazione telefonica.
`
