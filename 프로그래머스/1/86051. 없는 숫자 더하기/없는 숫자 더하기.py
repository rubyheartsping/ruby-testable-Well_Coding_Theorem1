def solution(numbers):

    exist = []
    for x in range(len(numbers)):
        exist.append(numbers.pop())

    return 45 - sum(exist)