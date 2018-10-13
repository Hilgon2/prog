file = open("Kaartnummers.txt", "w")

list = [
    "325255, Jan Jansen\n",
    "334343, Erik Materus\n",
    "235434, Ali Ahson\n",
    "645345, Eva Versteeg\n",
    "534545, Jan de Wilde\n",
    "345355, Henk de Vries\n"]

for item in list:
    file.write(item)
file.close()