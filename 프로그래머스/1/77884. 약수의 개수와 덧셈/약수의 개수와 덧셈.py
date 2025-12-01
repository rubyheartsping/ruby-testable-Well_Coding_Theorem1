from math import sqrt

def solution(left, right):
    num = 0
    for x in range(right - left + 1):
        if sqrt(left + x) == round(sqrt(left + x)):
            num = num - (left + x)

        else:
            num = num + (left + x)

    return num
