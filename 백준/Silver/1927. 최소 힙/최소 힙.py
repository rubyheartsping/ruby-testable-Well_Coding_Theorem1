import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    command = int(input())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, command)