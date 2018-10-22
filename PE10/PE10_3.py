import csv

gamerName = ""
gameDate = ""
number = 0
list = []

with open("file.csv", "r") as csvFile:
    reader = csv.reader(csvFile, delimiter=";")

    for row in reader:
        name = row[0]
        date = row[1]
        score = row[2]

        if int(score) > int(number):
            gamerName = name
            gameDate = date
            number = score

    print("De hoogste score is: " + str(number) + " op " + str("gameDate") + " behaald door " + gamerName)
