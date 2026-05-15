def solution(rows, columns, queries):
    
    def rotate(arr, query):
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        cur_x, cur_y = x1, y1
        state = 0
        candidate = []
        while len(candidate) < (x2 - x1 + y2 - y1) * 2:
            if type(arr[cur_x][cur_y]) == int:
                if state == 0:
                    if cur_x != x2:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x + 1][cur_y]]
                        cur_x += 1
                    else:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x][cur_y + 1]]
                        cur_y += 1
                        state = 1
                
                elif state == 1:
                    if cur_y != y2:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x][cur_y + 1]]
                        cur_y += 1
                    else:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x - 1][cur_y]]
                        cur_x -= 1
                        state = 2
                
                elif state == 2:
                    if cur_x != x1:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x - 1][cur_y]]
                        cur_x -= 1
                    else:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x][cur_y - 1]] if type(arr[cur_x][cur_y - 1]) == int else [arr[cur_x][cur_y], arr[cur_x][cur_y - 1][0]]
                        cur_y -= 1
                        state = 3
                        if cur_y == y1:
                            state = 0
                
                elif state == 3:
                    if cur_y != y1:
                        arr[cur_x][cur_y] = [arr[cur_x][cur_y], arr[cur_x][cur_y - 1]] if type(arr[cur_x][cur_y - 1]) == int else [arr[cur_x][cur_y], arr[cur_x][cur_y - 1][0]]
                        cur_y -= 1
                        if cur_y == y1:
                            state = 0
                    else:
                        state = 0
                
            
            elif type(arr[cur_x][cur_y]) == list:

                if state == 0:
                    if cur_x != x2:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_x += 1
                    else:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_y += 1
                        state = 1
                
                elif state == 1:
                    if cur_y != y2:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_y += 1
                    else:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_x -= 1
                        state = 2
                
                elif state == 2:
                    if cur_x != x1:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_x -= 1
                    else:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1]
                        candidate.append(arr[cur_x][cur_y])
                        cur_y -= 1
                        state = 3
                
                elif state == 3:
                    if cur_y != y1:
                        arr[cur_x][cur_y] = arr[cur_x][cur_y][1] 
                        candidate.append(arr[cur_x][cur_y])
                        cur_y -= 1
                        if cur_y == y1:
                            break
                    else:
                        break
            
                
        return arr, min(candidate)

    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows * columns):
        x, y = i // columns, i % columns
        arr[x][y] = i + 1
    answer = []
    for query in queries:
        arr, minimum = rotate(arr, query)
        answer.append(minimum)
    return answer
