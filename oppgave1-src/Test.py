import random
from BinaertSoketre import BinaertSoketre

def enkelTest():
    tre = BinaertSoketre()
    tre.insert(5)
    tre.insert(3)
    #print("leter etter 5")
    assert tre.contains(5)
    #print("leter etter 3")
    assert tre.contains(3)
    #print("leter etter 1")
    assert not tre.contains(1)
    tre.insert(2)
    tre.remove(3)
    assert not tre.contains(3)

def storTest():
    tre = BinaertSoketre()

    liste = set()

    antall = 10000
    for i in range(antall):
        tall = random.randint(1, 100000)
        liste.add(tall)
        tre.insert(tall)
        print(tall)

    print("\nInneholder " + str(antall) + "\nUtforer test:")

    #Tester contains
    for tall in liste:
        if not tre.contains(tall):
            print("Fant ikke " + str(tall))
    
    #Tester remove
    for tall in liste:
        tre.remove(tall)
        assert not tre.contains(tall)

storTest()