from itertools import permutations

def solution(k, dungeons):
    answer = 0
    ways = list(permutations(dungeons))
    for way in ways:
        health = k
        count = 0
        while count <= len(way) - 1 and health - way[count][1] >= 0 and health >= way[count][0]:
            health -= way[count][1]
            count += 1
        answer = max([answer, count])
    return answer
            