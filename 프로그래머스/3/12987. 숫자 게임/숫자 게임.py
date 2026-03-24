from collections import deque

def solution(A, B):
    A = deque(sorted(A, reverse = True))
    B = deque(sorted(B, reverse = True))
    count = 0
    while A:
        enemy = A.popleft()
        if B[0] > enemy:
            B.popleft()
            count += 1
        else:
            B.pop()
    return count