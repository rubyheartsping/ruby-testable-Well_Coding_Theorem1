import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    cabbages = set()
    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.add((x, y))

    worms = 0
    # 배추 좌표를 하나씩 꺼내서, 그 배추가 속한 덩어리를 BFS로 싹 지움
    while cabbages:
        start = cabbages.pop()
        worms += 1

        q = deque([start])
        while q:
            x, y = q.popleft()
            for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (nx, ny) in cabbages:
                    cabbages.remove((nx, ny))  # 방문 처리 (다시 안 보게)
                    q.append((nx, ny))

    print(worms)
