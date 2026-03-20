def solution(n, k):
    
    def to_base_k(n, k):
        place = 1 
        order = 1
        while place * k <= n:
            place *= k
            order += 1
        i = 0
        base_k_number = [0] * order 
        while n != 0:
            if n >= place:
                n -= place
                base_k_number[i] += 1
            else:
                place /= k
                i += 1
        return "".join(list(map(str, base_k_number)))
    
    def find_prime(number):
        if number == 0 or number == 1:
            return False
        i = 2
        while i ** 2 <= number:
            if number % i == 0:
                return False
            i += 1
        
        return True
    
    def find_candidate(str_number):
        result = str_number.split("0")
        for i in range(result.count("")):
            result.remove("")
        return list(map(int, result))
        
    
    answer = 0
    for number in find_candidate(to_base_k(n, k)):
        if find_prime(number):
            answer += 1
    
    return answer
    
