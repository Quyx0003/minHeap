import sys
import PQHeap

pq = PQHeap.createEmptyPQ()
n = 0
for line in sys.stdin:
    PQHeap.insert(pq,int(line))
    n = n+1

print()
while n > 0:
    print(PQHeap.extractMin(pq))
    n = n-1