def som(getallenLijst):
    getal = 0
    for som in getallenLijst:
        getal += som

    return getal

print(som([5, 10, 15, 50]))