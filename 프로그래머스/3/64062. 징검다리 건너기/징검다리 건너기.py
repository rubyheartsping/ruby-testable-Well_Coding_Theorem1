from collections import deque

def solution(stones, k):
    dq = deque()
    candidate = []
    for idx, stone in enumerate(stones):
        while dq and stones[dq[-1]] < stone:
            dq.pop()
        dq.append(idx)
        if idx - k >= dq[0]:
            dq.popleft()
        if idx >= k -1:
            candidate.append(stones[dq[0]])
    return min(candidate)
        