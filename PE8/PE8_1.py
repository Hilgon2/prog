number = 10
oldNumber = 0
amount = -1

while number != 0:
    number = int(input("Geef een getal: "))
    amount += 1
    oldNumber += number

print("Er zijn " + str(amount) + " getallen ingevoerd, de som is: " + str(oldNumber))