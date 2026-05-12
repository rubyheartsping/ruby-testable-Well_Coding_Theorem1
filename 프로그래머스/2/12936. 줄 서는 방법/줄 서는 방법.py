from math import factorial, ceil

def solution(n, k):
    answer = []
    inspector = factorial(n)
    numbers = [i for i in range(n + 1)]
    for i in range(-n, 0):
        inspector //= -i
        if numbers[ceil(k / inspector)] != 0:
            answer.append(numbers[ceil(k / inspector)])
            numbers.remove(numbers[ceil(k / inspector)])
        else:
            answer.append(numbers[-1])
            numbers.remove(numbers[-1])
        k %= inspector
    
    return answer
    
        