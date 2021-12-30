# Translator
## Introduction
This is  a guide to install and use this translator for bash terminal.
***
## Installation
1. Install the library of google trans: (install pip if it isn't yet installed!) <br>
`pip install googletrans==4.0.0-rc1` 
2. Move the program in the `/bin` folder with `cp` command
3. Add in the file `.bashrc` located on `/home` folder the folllowing line: <br>
`alias translate="python3 /bin/translate.py"`
***
## How to use

Insert the translate keyword `translate` + source language + destination language + phrase to translate

Example: <br>
`$ translate en it hello` <br>

Result: <br>
`Translation of 'hello': Ciao
` 
<br>
<br>

If you want translate a phrase surround it with a double quotes `""`<br>

Example: <br>
`$ translate en it "Hello World"`<br>

Result: <br>
`translate en it "Hello World"
`
