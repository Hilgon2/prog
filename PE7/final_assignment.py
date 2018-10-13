file = open("kluisjes.txt", "r+")
maxLockers = 12

def menu():
    invoer = int(input("Kies uw menukeuze: \n"
                       "1: Ik wil weten hoeveel kluizen nog vrij zijn \n"
                       "2: Ik wil een nieuwe kluis \n"
                       "3: Ik wil even iets uit mijn kluis halen \n"
                       "4: Ik geef mijn kluis terug \n"))

    keuzes = [1, 2, 3, 4]
    if invoer not in keuzes:
        return print("Kies een getal tussen de 1 en 4")
    elif invoer == 1:
        freeLockers()
    elif invoer == 2:
        newLocker()
    elif invoer == 3:
        useLocker()
    elif invoer == 4:
        returnLocker()


def freeLockers():
    print("Er zijn " + str(maxLockers - len(file.readlines())) + " kluizen beschikbaar")


def newLocker():
    lockerNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    lockersList = []

    invoer = input("Vul uw code in voor uw kluis")
    if len(invoer) < 4:
        return print("Uw code moet minimaal 4 tekens lang zijn")

    for nummer in file.readlines():
        getal = nummer.split(";")[0]
        lockersList.append(int(getal))
    lockersList.sort()

    for lockerNumber in lockerNumbers:
        if lockerNumber not in lockersList:
            file.write("\n" + str(lockerNumber) + ";" + invoer)
            return


def useLocker():
    inputNumber = input("Vul uw kluisnummer in")
    inputCode = input("Vul uw kluiscode in")

    for nummer in file.readlines():
        locker = nummer.split(";")
        if inputNumber == locker[0]:
            if inputCode == locker[1].split("\n")[0]:
                return print("U krijgt toegang tot uw kluis")
            else:
                return print("Code incorrect")


def returnLocker():
    inputNumber = input("Vul uw kluisnummer in")
    inputCode = input("Vul uw kluiscode in")
    returnedLocker = ""
    newLockers = []

    for line in file.readlines():
        locker = line.split(";")
        if inputNumber == locker[0]:
            if inputCode == locker[1].split("\n")[0]:
                returnedLocker = line
                print("Uw kluis is weer teruggegeven")
            else:
                return print("Code incorrect")
        if returnedLocker != line:
            newLockers.append(line)

    fileWrite = open("kluisjes.txt", "w")

    for s in newLockers:
        fileWrite.write(s)

menu()
file.close()
