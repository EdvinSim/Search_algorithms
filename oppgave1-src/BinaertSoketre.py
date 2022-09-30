#IN2010, innleveringsoppgave 1, oppgave 1a

class BinaertSoketre:

    def __init__(self):
        self._root = None
        self._size = 0 #Siden size skal veare O(1).

    def contains(self, x):
        if self._find(self._root, x) == None:
            print("false") #str istedenfor bool siden inputfilen er smaa bokstaver.
        else:
            print("true")

    #Privat hjelpemetode
    #Leter gjennom treet og returnerer enten noden med samme nummer eller None hvis den ikke finnes.
    def _find(self, node, x):
        num = node.data

        if node == None:
            return None
        elif num == x:
            return node
        elif node.right != None and x > num:
            return self._find(node.right, x)
        elif node.left != None and x < num:
            return self._find(node.left, x)
        else:
            return None

    def insert(self, x):
        if self._root == None:
            self._root = self.Node(x, None)
            self._size += 1
        else:
            self._put(self._root, x)
    
    #Privat hjelpemetode
    def _put(self, node, x):
        if node.data == x: #Da finnes den fra foer.
            #print(str(x) + " finnes fra foer") #TODO fjern
            return
        elif x > node.data:
            if node.right == None:
                node.right = self.Node(x, node)
                self._size += 1
            else:
                self._put(node.right, x)
        elif x < node.data:
            if node.left == None:
                node.left = self.Node(x, node)
                self._size += 1
            else:
                self._put(node.left, x)


    def remove(self, x):
        self._root = self._remove(self._root, x)


    #Privat hjelpemetode
    def _remove(self, node, x):
        if node == None: #Hvis vi forsoeker aa fjerne noe som ikke er der.
            return None
        elif x < node.data:
            node.left = self._remove(node.left, x)
            return node
        elif x > node.data:
            node.right = self._remove(node.right, x)
            return node

        #Node med et eller ingen barn
        elif node.left == None:
            self._size -= 1
            return node.right
        elif node.right == None:
            self._size -= 1
            return node.left

        #Noden vi vil slette har 2 barn
        else:
            replace = self._findLow(node.right)
            node.data = replace.data
            node.right = self._remove(node.right, replace.data)
            return node

    def _findLow(self, node):
        if node.left == None:
            return node
        else:
            return self._findLow(node.left)

    def size(self):
        print(self._size)

    #Indre klasse
    class Node:
        def __init__(self, data, parent):
            self.data = data
            self.parent = parent #TODO trengs kanskje ikke alikevel
            self.right = None
            self.left = None

        def __str__(self):
            return str(self.data)

#Bruk til testing med input og outputfiler.
def main():
    tre = BinaertSoketre()
    NumOperations = input()
    operations = {"size": tre.size, "contains": tre.contains, "insert": tre.insert, "remove": tre.remove}

    def operation(inputline: str):
            if inputline == "size":
                operations[inputline]()
            else:
                line = inputline.split()
                operations[line[0]](line[1])

    for i in range(int(NumOperations)):
        inputline = input().strip()
        operation(inputline)

main()