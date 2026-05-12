def solution(data, col, row_begin, row_end):
    if col != 1:
        data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    else:
        data = sorted(data, key = lambda x : x[col-1])
    
    hash_list = []
    for i in range(row_begin-1, row_end):
        for j in range(len(data[0])):
            data[i][j] = data[i][j] % (i + 1)
        hash_list.append(sum(data[i]))
    
    cur = hash_list[0]
    for i in range(1, len(hash_list)):
        cur = cur ^ hash_list[i]
    
    return cur
    
    