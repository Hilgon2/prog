file = open("Kaartnummers.txt", "r")
fileItems = file.readlines()
print("Deze file telt " + str(len(fileItems)) + " regels")
number = 0
line = 1
for item in fileItems:
    lineItem = item.replace("\n", "").split(",")
    if int(lineItem[0]) > int(number):
        number = lineItem[0]
        line = line + 1

print("Het grootste kaartnummer is: " + str(number) + " en dat staat op regel " + str(line))
file.close()