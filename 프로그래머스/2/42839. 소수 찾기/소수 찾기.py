from itertools import permutations

def solution(numbers):
    
    def find_prime(number: int):
        j = 2
        if number in [0, 1]:
                return False
        elif number in [2, 3]:
            return True
        while j ** 2 <= number:
            if number % j == 0:
                return False
            j += 1
        return True
    
    answer = 0
    numbers = list(numbers)
    candidates = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            candidates.add(int("".join((p))))
    print(candidates)
    for candidate in candidates:
        if find_prime(candidate) == True:
            answer += 1
    return answer