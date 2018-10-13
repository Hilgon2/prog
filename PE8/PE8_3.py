dict = {"Terry": 10,
        "Esben": 9.5,
        "Justin": 9.7,
        "Colin": 9.1,
        "Martijn": 6,
        "Henk": 3.2,
        "Sara": 1,
        "Bob": 2.9,
        "Klaas": 10,
        "Dirk": 9.0}

for item in dict:
    if float(dict[item]) > 9:
        print(str(item) + ": " + str(dict[item]))