age = int(input("Geef je leeftijd"))
passport = input("Nederlands paspoort (ja/nee)")

if age >= 18 and passport == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag niet stemmen")