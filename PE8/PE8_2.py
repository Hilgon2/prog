word = input("Geef een string van vier letters: ")

while len(word) != 4:
    print(str(word) + " heeft " + str(len(word)) + " letters")
    word = input("Geef een string van vier letters: ")

print("Inlezen van correcte string: " + word + " is geslaagd")