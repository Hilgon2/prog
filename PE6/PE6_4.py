import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")

def hardloper(naam):
    file = open('hardlopers.txt', 'a')
    file.write(s + naam + "\n")
    file.close()

hardloper("Justin")