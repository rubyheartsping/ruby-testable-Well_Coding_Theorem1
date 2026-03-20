def solution(numbers):
    stack = [numbers[-1]]
    result = [-1] * len(numbers)
    for i in range(2, len(numbers) + 1):
        while stack and stack[-1] <= numbers[-i]:
            stack.pop()
        if stack:
            result[-i] = stack[-1]
        
        stack.append(numbers[-i])

    return result