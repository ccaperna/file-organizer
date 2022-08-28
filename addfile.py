#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import csv
import argparse
import sys
import numpy as np

try:
    #creazione di un oggetto di tipo argparse       
    parser = argparse.ArgumentParser(description = "Sposta un file nella cartella corrispondente")
    #assegnazione argomenti
    parser.add_argument("-f", "--file", type = str, help = "Nome del file + estensione", required = True)
    file = sys.argv[2]
    args = parser.parse_args()
    #print(type(args))
except argparse.ArgumentError:
    print("Errore, il file non esiste")
#inizializzo un dizionario e le liste che saranno i valori del diz
diz = dict()
nome = []
tipo = []
grand = []
#memorizzo il percorso sorgente
source = "C:\\FileOrganizer"
fl = os.path.join(source,"files")
#trovo la directory contenente i file di interesse
files = os.listdir(fl)
#creazione cartelle con controllo
if not os.path.isdir(os.path.join(fl, "Docs")):
    os.mkdir(os.path.join(fl, "Docs"))
if not os.path.isdir(os.path.join(fl, "Images")):
    os.mkdir(os.path.join(fl, "Images"))
if not os.path.isdir(os.path.join(fl, "Audio")):
    os.mkdir(os.path.join(fl, "Audio"))
#scorro i file all'interno della dir per processarli 
if file in files:
    name = os.path.splitext(os.path.basename(file))[0]
    #controllo per creare una nuova dir e spostare il file
    #raccolgo info dai file
    #aggiorno le liste con le informazioni dei file
    if (file.endswith((".txt",".odt"))):
        size = os.path.getsize(os.path.join(fl,file))
        shutil.move(f"{fl}\\{file}", os.path.join(fl, "Docs"))
        print(name, "type: doc", "size: ",size, "B")
        nome.append(name)
        tipo.append("doc")
        grand.append(size)
        print("File spostato con successo")      
    if (file.endswith((".png",".jpeg",".jpg"))):
        size = os.path.getsize(os.path.join(fl,file))
        shutil.move(f"{fl}\\{file}", os.path.join(fl,"Images"))
        print(name, "type: image", "size: ",size, "B")
        nome.append(name)
        tipo.append("image")
        grand.append(size)
        print("File spostato con successo")
    if (file.endswith(".mp3")):
        size = os.path.getsize(os.path.join(fl,file))
        shutil.move(f"{fl}\\{file}", os.path.join(fl,"Audio"))
        print(name, "type: audio", "size: ",size, "B")
        nome.append(name)
        tipo.append("audio")
        grand.append(size)
        print("File spostato con successo")     
#aggiorno il dizionario 
diz["Nome"] = nome
diz["Tipo"] = tipo
diz["Grandezza"] = grand
#creazione documento csv e/o aggiornamento
if os.path.isfile(os.path.join(source,"recap.csv")):
     with open("recap.csv", "a") as recap:
         #creazione oggetto writer per scrivere sul file
         writer = csv.writer(recap)
         #scrivo i valori sulle righe
         writer.writerows(zip(*diz.values()))
else:
     with open("recap.csv", "w") as recap:
        writer = csv.writer(recap)
        #scrivo l'"intestazione" data dalle chiavi del diz
        writer.writerow(diz.keys())
        writer.writerows(zip(*diz.values()))

