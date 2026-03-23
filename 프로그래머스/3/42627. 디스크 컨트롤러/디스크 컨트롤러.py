import heapq
from collections import deque

def solution(jobs):
    len_jobs = len(jobs)
    result = []
    jobs = sorted(jobs, key = lambda x: [x[0], x[1]])
    jobs = deque(jobs)
    time = 0
    pq = []
    done = 0
    while done < len_jobs:
        while jobs and jobs[0][0] <= time:
            temp = jobs.popleft()
            heapq.heappush(pq, [temp[1], temp[0]])

        if pq:
            cur = heapq.heappop(pq)
            time += cur[0]
            done += 1
            result.append(time - cur[1])
        else:
            time = jobs[0][0]

    return sum(result) // len(result)