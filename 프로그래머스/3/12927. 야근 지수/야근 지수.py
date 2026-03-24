import heapq

def solution(n, works):
    pq = []
    if sum(works) <= n:
        return 0
    for work in works:
        heapq.heappush(pq, -work)
    while n != 0:
        n -= 1
        temp = heapq.heappop(pq) + 1
        heapq.heappush(pq, temp)
    
    result = 0
    for work in pq:
        result += work ** 2
    return result