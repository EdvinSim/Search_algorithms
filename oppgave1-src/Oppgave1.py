
from BinaertSoketre import BinaertSoketre

#Denne fungerer kun hvis man ikke kjorer main() i BinaertSoketre.py

tree = BinaertSoketre()

filename = input("Filnavn: ")
file = open(filename, "r")
operations = (int(file.readline()))

#TODO skjer noe feil her. Den prøver aa fjerne 744387, men sier at den ikke finnes selv om den ble satt inn tidligere. 

#Her trenger man bare inputfilen.
def withoutTest():
    for x in range(operations):
        line = file.readline().strip().split(" ")
        command = line[0]
        if command == "size":
            print(tree.size())
        elif command == "insert":
            tree.insert(line[1])
        elif command == "remove":
            tree.remove(line[1])
        elif command == "contains":
            print(tree.contains(line[1]))
        else:
            print("Feil i avslesning")

#Her maa man ha baade input- og outputfil tilgjengelig siden den sjekker input mot expectedoutput.
def test():
    fileSize =  filename.split("_")[1]

    outputFile = open("outputs/output_" + fileSize , "r")

    for x in range(operations):
        line = file.readline().strip().split(" ")
        command = line[0]

        if command == "size":
            expectedOutput = outputFile.readline().strip()
            actualOutput = str(tree.size())
            print(actualOutput)
            assert actualOutput == expectedOutput, str(line) + ": [actual = " + actualOutput + ", expected = " + expectedOutput + "]"
        
        elif command == "insert":
            tree.insert(line[1])
            #print(str(line) + " size: " + str(tree.size()))
        
        elif command == "remove":
            tree.remove(line[1])
            #print(str(line) + " size: " + str(tree.size()))

        elif command == "contains":
            expectedOutput = outputFile.readline().strip()
            actualOutput =  str(tree.contains(line[1])).lower()
            print(actualOutput)
            assert actualOutput == expectedOutput, str(line) + ": [actual = " + actualOutput + ", expected = " + expectedOutput + "]"
        
        else:
            print("Feil i avslesning")

test()
#withoutTest()