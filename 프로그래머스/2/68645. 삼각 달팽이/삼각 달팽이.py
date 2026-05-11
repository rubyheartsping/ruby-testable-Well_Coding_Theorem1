def solution(n):
    triangle = []
    for i in range(n):
        triangle.append([0] * (i + 1))
    limit = n
    count = 0
    direction = 0
    cur = [0, 0]
    for i in range(n * (n + 1) // 2):
        triangle[cur[0]][cur[1]] = i + 1
        count += 1
        if direction == 0:
            if count == limit:
                count = 0
                limit -= 1
                direction = 1
                cur[1] += 1
            else:
                cur[0] += 1
        
        elif direction == 1:
            if count == limit:
                count = 0
                limit -= 1
                direction = 2
                cur[0] -= 1
                cur[1] -= 1
            else:
                cur[1] += 1
        
        else:
            if count == limit:
                count = 0
                limit -= 1
                direction = 0
                cur[0] += 1
            else:
                cur[0] -= 1
                cur[1] -= 1
    answer = []
    for arr in triangle:
        answer += arr
    return answer
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    