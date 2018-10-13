def code(invoerstring):
    string = ""
    for letter in invoerstring:
        ascii = ord(letter)
        encryption = ascii + 3
        string += chr(encryption)
    print(string)

code('RutteAlkmaarDen Helder')