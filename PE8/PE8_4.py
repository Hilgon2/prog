writeFile = open("companies.txt", "w+")
companies = {"YAHOO": "YHOO",
            "GOOGLE INC": "GOOG",
            "Harley-Davidson": "HOG",
            "Yamana Gold": "AUY",
            "Sotheby's": "BID",
            "inBev": "BUD"}

for company in companies:
    writeFile.write(company + ":" + companies[company] + "\n")
writeFile.close()

dict = {}

def ticker(filename):
    readFile = open(filename, "r")

    for company in readFile.readlines():
        name = company.strip("\n")
        splitName = name.split(":")
        dict[splitName[0]] = splitName[1]

    readFile.close()

def tickerInput():
    ticker = input("Enter company name: ")

    for company in dict:
        if ticker == company:
            print("Ticker symbol: " + str(dict[company]))

    companyInput = input("Enter Ticker symbol: ")
    for company in dict:
        if dict[company] == companyInput:
            print("Company name: " + str(company))

ticker("companies.txt")
tickerInput()


