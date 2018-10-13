stations = [
    "Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk",
    "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven",
    "Weert", "Roermond", "Sittard", "Maastricht"]

def getStartingStation(stations):
    value = False

    while not value:
        startStation = input("Vanaf welk station wil u reizen? ")
        if startStation in stations:
            return startStation


def getEndingStation(stations, startingStation):
    value = False

    while not value:
        endingStation = input("Naar welk station wil u reizen? ")
        if endingStation in stations and stations.index(endingStation) > stations.index(startingStation):
            return endingStation
        else:
            print("Deze trein komt niet in " + endingStation)


def travelInformation(stations, startingStation, endingStation):
    startStationNumber = stations.index(startingStation)
    endStationNumber = stations.index(endingStation)
    stationsDifference = endStationNumber - startStationNumber
    price = stationsDifference * 5
    count = startStationNumber + 1

    print("Het beginstation " + startingStation + " is het " + str(startStationNumber + 1) + "e station in het traject.")
    print("Het beginstation " + endingStation + " is het " + str(endStationNumber + 1) + "e station in het traject.")
    print("De afstand bedraagt " + str(stationsDifference) + " station(s).")
    print("De prijs van het kaartje is " + str(price) + " euro. \n")

    print("Jij stapt in de trein in: " + startingStation)
    while endStationNumber > count:
        print(" - " + stations[count])
        count += 1
    print("Jij stapt uit in: " + endingStation)


startingStation = getStartingStation(stations)
endingStation = getEndingStation(stations, startingStation)
travelInformation(stations, startingStation, endingStation)