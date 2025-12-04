def solution(a, b, n):
    answer = 0
    empty = n
    
    while empty >= a:
        new = (empty // a) * b
        answer += new
        empty = (empty % a) + new
    
    return answer
