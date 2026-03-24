from collections import deque

def solution(routes):
    routes = deque(sorted(routes, key = lambda x : x[1]))
    count = 0
    while routes:
        count += 1
        camera = routes.popleft()[1]
        while routes:
            if camera >= routes[0][0] and camera <= routes[0][1]:
                routes.popleft()
            else:
                break
    return count
            