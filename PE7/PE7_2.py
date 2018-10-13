lijst = eval(input("Geef lijst met minimaal 10 strings: "))
list = []

for string in lijst:
    if len(string) == 4:
        list.append(string)

print("De nieuw-gemaakte lijst met alle vier-letter strings is:" + str(list))