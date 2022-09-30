#IN2010 innleveringsoppgave 1, oppgave 2b

import math

class Teque:

    def __init__(self):
        self._first = None
        self._middle = None
        self._last = None
        self._teque = []

    #Her antar jeg at vi ikke skal bruke python sine innebygde metoder for aa sette inn.
    #Evt. bare .append().
    def push_back(self, x):
        size = len(self._teque)
        self._teque.append(None)
        self._teque[size] = x
        self._last = self._teque[size]

    def push_front(self, x):
        size = len(self._teque)
        self._teque.append(None)

        for i in range(size):
            self._teque[size - i] = self._teque[size - 1 - i]
        
        self._teque[0] = x
        self._front = self._teque[0]

    def push_middle(self, x):
        #Hvis teque er tom.
        if len(self._teque) == 0:
            self.push_front(x)
            return

        size = len(self._teque)
        self._teque.append(None)

        for i in range(math.ceil(size/2)):
            self._teque[size - i] = self._teque[size - 1 - i]
        
        self._teque[math.floor((size+1)/2)] = x
        self._middle = self._teque[math.floor(size/2)]

    def get(self, x):
        #TODO hva hvis x ikke finnes?
        return self._teque[int(x)]

    def __str__(self):
        return str(self._teque)


def main():
    teque = Teque()
    operations = input()

    for i in range(int(operations)):
        inputline = input().strip().split(" ")

        if inputline[0] == "push_back":
            teque.push_back(inputline[1])
        elif inputline[0] == "push_front":
            teque.push_front(inputline[1])
        elif inputline[0] == "push_middle":
            teque.push_middle(inputline[1])
        elif inputline[0] == "get":
            print(teque.get(inputline[1]))
        else:
            print("Feil i innlesning!")

main()