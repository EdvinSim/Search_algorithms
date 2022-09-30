from Teque import Teque

filename = input("Filnavn: ")
inputFile = open(filename)
numberOfCommands = int(inputFile.readline())
teque = Teque(numberOfCommands)

outputFile = open("outputs/output_" + filename.split("_")[1])

for i in range(numberOfCommands):
    linje = inputFile.readline().strip().split(" ")
    num = linje[1]

    if linje[0] == "push_back":
        teque.push_back(num)
    elif linje[0] == "push_front":
        teque.push_front(num)
    elif linje[0] == "push_middle":
        teque.push_middle(num)

    elif linje[0] == "get":
        exptectedOut = outputFile.readline().strip()
        if teque.get(num) != exptectedOut:
            print("Forsokte " + str(linje) + " forventet: " + exptectedOut)
            print(teque)
