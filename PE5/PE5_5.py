list = [4, 5, 3, -81]

def kwadraten_som(grondgetallen):
    getal = 0
    for nummer in list:
        if nummer >= 0:
            kwadraat = nummer * nummer
            getal += kwadraat

    return getal

print(kwadraten_som(list))