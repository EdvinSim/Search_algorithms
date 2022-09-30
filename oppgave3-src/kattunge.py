#IN2010 innleveringsoppgave 1, oppgave 3b

def escape_route():

    #I nodeliste er index tallet til noden og valuen forelderen.
    nodeliste = [None]*101
    katt = int(input().strip())
    line = input().strip().split(" ")

    #Setter foreldre og bygger treet
    while line[0] != "-1":
        for num in line[1:]:
            nodeliste[int(num)] = int(line[0])
        line = input().strip().split(" ")
    
    #Printer rute
    exit = ""

    while katt != None:
        exit += str(katt) + " "
        katt = nodeliste[katt]

    print(exit.strip())

escape_route()