def gemiddelde(zin):
    zinList = zin.split()
    lenList = []
    for woord in zinList:
          lengte = len(woord)
          lenList.append(lengte)
    resultaat = sum(lenList) / len(lenList)
    print(resultaat)

gemiddelde("Hallo ik ben Terry")