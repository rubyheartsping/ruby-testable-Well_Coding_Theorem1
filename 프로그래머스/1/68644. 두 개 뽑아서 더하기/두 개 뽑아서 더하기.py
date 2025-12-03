def solution(numbers):
    lst = []
    sumset = set()
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            lst.append([numbers[x], numbers[y]])

    for z in lst:
        sumset.add(sum(z))

    answer = sorted(list(sumset))
    return answer