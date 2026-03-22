def solution(clothes):
    dict_clothe = {}
    for clothe in clothes:
        dict_clothe[clothe[1]] = 0
    
    for clothe in clothes:
        dict_clothe[clothe[1]] += 1
    
    answer = 1
    for num in dict_clothe.values():
        answer *= (num + 1)
    return answer - 1
    