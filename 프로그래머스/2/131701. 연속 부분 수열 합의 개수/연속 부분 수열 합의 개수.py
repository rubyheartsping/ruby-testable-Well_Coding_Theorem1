def solution(elements):
    len_elements = len(elements)
    elements = elements * 2
    answer = set()
    for i in range(1, len_elements + 1):
        for j in range(len_elements):
            answer.add(sum(elements[j : i + j]))
    
    return len(answer)
            