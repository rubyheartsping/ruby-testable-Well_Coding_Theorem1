def solution(numbers):
    
    def key(number):
        if number < 10:
            return number * 111111
        elif number < 100:
            return number * 10101
        elif number < 1000:
            return number * 1001
        else:
            return 1
    
    numbers = list(map(str, sorted(numbers, key = key, reverse = True)))
    return str(int("".join(numbers)))