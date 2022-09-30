import math

#IN201O innleveringsoppgave 1, oppgave 4a

def balance(list):
    midIndex = math.floor(len(list)/2)
    print(list[midIndex])

    #Naar array er et element.
    if midIndex == 0:
        return

    #Naar det er 2 elementer i array
    elif midIndex == 1:
        print(list[0])
        
    else:
        right = list[midIndex + 1:]
        left = list[:midIndex]
        balance(right)
        balance(left)

def smallTest():
    list = []
    for num in range(11):
        list.append(num)

    balance(list)

def test():
    list = []
    
    #Her maa range vaere samme som seq naar man kjorer testprogrammet BalanceChecker.
    for line in range(20):
        line = input().strip()
        list.append(line)
        
    balance(list)

test()
