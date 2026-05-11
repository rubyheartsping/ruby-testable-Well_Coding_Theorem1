from collections import Counter
from itertools import combinations

def solution(weights):
    weights = Counter(weights)
    sort_weights = []
    for weight in weights.keys():
        if weights[weight] == 1:
            sort_weights.append(weight)
        else:
            sort_weights.append(weight)
            sort_weights.append(weight)
    nCr = combinations(sort_weights, 2)
    ways = list(nCr)
    available = set()
    for way in ways:
        way = tuple(sorted(way))
        if way[0] == way[1]:
            available.add(way)
        elif way[0] * 3 / 2 == way[1]:
            available.add(way)
        elif way[0] * 4 / 3 == way[1]:
            available.add(way)
        elif way[0] * 2 == way[1]:
            available.add(way)
    
    answer = 0
    for avail in available:
        if avail[0] == avail[1]:
            answer += weights[avail[0]] * (weights[avail[0]] - 1) / 2
        else:
            answer += weights[avail[0]] * weights[avail[1]]
    print(available)
    return answer
    