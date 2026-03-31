def solution(gems):
    kinds = len(set(gems))
    length = len(gems)
    answer = [1,  length]
    
    gems_count = {}
    left = 0
    
    for right in range(length):
        gems_count[gems[right]] = gems_count.get(gems[right], 0) + 1
        
        while len(gems_count) == kinds:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left + 1, right + 1]
                
            gems_count[gems[left]] -= 1
            if gems_count[gems[left]] == 0:
                del gems_count[gems[left]]
            
            left += 1
    return answer