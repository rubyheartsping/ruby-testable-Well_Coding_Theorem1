from collections import deque

def solution(priorities, location):
    dq = deque((p, i) for i, p in enumerate(priorities))
    count = 0

    while True:
        cur = dq.popleft()

        if any(cur[0] < x[0] for x in dq):
            dq.append(cur)
        else:
            count += 1
            if cur[1] == location:
                return count
