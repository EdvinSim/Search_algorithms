#IN2010 innlevering 1, oppgave 4b

import heapq, math

def heapBalance(heap :heapq):
    size = len(heap)

    if size == 1:
        print(heapq.heappop(heap))
    else:
        rightHeap = heap
        leftHeap = []
        heapq.heapify(leftHeap)

        for i in range(math.floor(size/2)):
            tmp = heapq.heappop(rightHeap)
            heapq.heappush(leftHeap, tmp)
        
        print(heapq.heappop(rightHeap))

        if len(rightHeap) > 0:
            heapBalance(rightHeap)
        heapBalance(leftHeap)


def main():
    heap = []
    heapq.heapify(heap)

    #Her maa range vaere samme som seq naar man tester.
    for i in range(20):
        heapq.heappush(heap, int(input()))
        
    heapBalance(heap)

main()