def solution(s):
    stack = []
    prev = ""
    for c in s:
        if c == prev:
            stack.pop()
        else:
            stack.append(c)
        
        if stack:
            prev = stack[len(stack) - 1]
        else:
            prev = ""
    
    if stack:
        return 0
    else:
        return 1
        