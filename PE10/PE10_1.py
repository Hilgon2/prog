price = 4356
persons = input("Hoeveel personen gaan er mee?")

try:
    print(price / int(persons))
except:
    if not persons.isnumeric():
        print("Gebruik cijfers voor het invoeren van het aantal!")
    elif int(persons) == 0:
        print("Delen door nul kan niet!")
    elif int(persons) < 0:
        print("Negatieve getallen zijn niet toegestaan!")
    else:
        print("Onjuiste invoer!")