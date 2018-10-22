import datetime
import csv

bestand = 'inloggers.csv'

naam = input("Wat is je achternaam? ")
voorl = input("Wat zijn je voorletters? ")
gbdatum = input("Wat is je geboortedatum? ")
email = input("Wat is je e-mail adres? ")
date = datetime.datetime.now().strftime('%a %d %b %Y at %X')

with open("file.csv", "w" , newline="") as myFile:
    writer = csv.writer(myFile, delimiter=";")
    writer.writerow((date, naam, voorl, gbdatum, email))