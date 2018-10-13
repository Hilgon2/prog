def convert(celsius):
    return celsius * 1.8 + 32

def table():
    for degrees in range(-30, 50, 10):
        print("{:5} {:5}".format(convert(degrees), degrees))

table()