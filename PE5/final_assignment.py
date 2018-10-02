def standaardprijs(afstandKM):
    prijs = 0

    if afstandKM > 50:
        prijs = 15 + (0.60 * afstandKM)
    elif afstandKM < 0:
        prijs = 0
    else:
        prijs = 0.80 * afstandKM

    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    standPrijs = standaardprijs(afstandKM)
    prijs = 0

    if not weekendrit and (leeftijd < 12 or leeftijd >= 65):
        prijs = standPrijs / 100 * 30
    elif weekendrit and (leeftijd < 12 or leeftijd >= 65):
        prijs = standPrijs / 100 * 35
    elif not weekendrit and 12 < leeftijd < 65:
        prijs = standPrijs
    elif weekendrit and 12 < leeftijd < 65:
        prijs = standPrijs / 100 * 40

    return round(prijs, 2)

print(ritprijs(13, True, 20))