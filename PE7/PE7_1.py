def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        seizoen = "winter"
    elif maand == 3 or maand == 4 or maand == 5:
        seizoen = "lente"
    elif maand == 6 or maand == 7 or maand == 8:
        seizoen = "zomer"
    elif maand == 9 or maand == 10 or maand == 11:
        seizoen = "herfst"

    print(seizoen)

seizoen(2)