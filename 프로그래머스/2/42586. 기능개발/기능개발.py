from collections import deque

def solution(progresses, speeds):
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        temp = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for progress in progresses:
            if progress >= 100:
                temp += 1
            else:
                break
        for _ in range(temp):
            progresses.popleft()
            speeds.popleft()
        if temp != 0:
            result.append(temp)
    return result
            