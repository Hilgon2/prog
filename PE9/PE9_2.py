import random

def monopolyworp():

    count = 0
    value = False

    while not value:

        randomNumber1 = random.randrange(1, 7)
        randomNumber2 = random.randrange(1, 7)
        add = randomNumber1 + randomNumber2

        if count == 3:
            print("Derde keer dubbel: naar de gevangenis!")
            break

        if randomNumber1 == randomNumber2:
            print(str(randomNumber1) + " + " + str(randomNumber2) + " = " + str(add) + " (dubbel)")
            count += 1
        else:
            print(str(randomNumber1) + " + " + str(randomNumber2) + " = " + str(add))
            value = True

monopolyworp()