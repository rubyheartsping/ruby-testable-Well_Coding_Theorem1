def solution(s):
    answer = 0
    len_s = len(s)
    if len_s % 2 == 1:
        return 0
    for i in range(len_s):
        stack = []
        pair = s[i : ] + s[ : i]
        for c in pair:
            
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    break
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    return answer
                    
                    