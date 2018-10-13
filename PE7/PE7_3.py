invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
split = invoer.split("-")
list = []

for getal in split:
    list.append(int(getal))
    list.sort()

print("Gesorteerde list van ints: " + str(list))
print("Grootste getal: " + str(max(list)) + " en Kleinste getal: " + str(min(list)))
print("Aantal getallen: " + str(len(list)) + " en Som van de getallen: " + str(sum(list)))
print("Gemiddelde: " + str(sum(list) / len(list)))