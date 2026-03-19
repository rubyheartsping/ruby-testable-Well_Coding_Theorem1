from collections import deque

def solution(cacheSize, cities):
    answer = 0
    d = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if not d:
            d.append(city)
            answer += 5
        else:
            if city not in d:
                d.append(city)
                answer += 5
                if len(d) > cacheSize:
                    d.popleft()
            else:
                d.remove(city)
                d.append(city)
                answer += 1
    return answer

    