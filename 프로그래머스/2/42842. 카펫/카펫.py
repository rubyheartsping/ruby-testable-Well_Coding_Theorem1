def solution(brown, yellow):
    
    def condition(m, n):
        return [m * n - ((m - 2) * (n - 2)), (m - 2) * (n - 2)]
    i = 1
    total = brown + yellow
    weak_numbers = []
    while i ** 2 <= total:
        if total % i == 0:
            weak_numbers.append(i)
        i += 1
    for num in weak_numbers:
        if condition(total / num, num) == [brown, yellow]:
            return [total / num, num]