def solution(n, t, m, p):
    dic = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    def to_base_n(n, number):
        if n == 0:
            return 0
        result = []

        while True:
            if number % n < 10:
                result.append(str(number % n))
                number //= n
            elif number % n >= 10:
                result.append(dic[number % n])
                number //= n
            if number <= 0:
                break
        return reversed(result)
    
    def make_list(n, t, m, p):
        limit = (t - 1) * m + p
        numbers = []
        number = 0
        while len(numbers) < limit:
            numbers.extend(to_base_n(n, number))
            number += 1
        return numbers
    
    answer = []
    numbers = make_list(n, t, m, p)
    for i in range(t):
        answer.append(numbers[m*i+p-1])
    return "".join(answer)
        
    