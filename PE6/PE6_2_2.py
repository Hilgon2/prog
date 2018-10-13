file = open("Kaartnummers.txt", "r")

fileItems = file.readlines()

for item in fileItems:
    lineItem = item.replace("\n", "").split(",")
    print(lineItem[1] + " heeft kaartnummer: " + lineItem[0])

file.close()