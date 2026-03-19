from collections import deque

def solution(maps):
    dq = deque([[0, 0, 1]])
    maps[0][0] = 0
    while dq:
        p = dq.popleft()
        if (p[0] == len(maps) - 1) and (p[1] == len(maps[0]) - 1):
            return p[2]
        dn, ds, de, dw = [p[0] - 1, p[1]], [p[0] + 1, p[1]], [p[0], p[1] + 1], [p[0], p[1] - 1]
        if 0 <= dn[0] < len(maps) and 0 <= dn[1] < len(maps[0]) and maps[dn[0]][dn[1]] == 1:
            dq.append([dn[0], dn[1], p[2] + 1])
            maps[dn[0]][dn[1]] = 0
        if 0 <= ds[0] < len(maps) and 0 <= ds[1] < len(maps[0]) and maps[ds[0]][ds[1]] == 1:
            dq.append([ds[0], ds[1], p[2] + 1])
            maps[ds[0]][ds[1]] = 0
        if 0 <= de[0] < len(maps) and 0 <= de[1] < len(maps[0]) and maps[de[0]][de[1]] == 1:
            dq.append([de[0], de[1], p[2] + 1])
            maps[de[0]][de[1]] = 0
        if 0 <= dw[0] < len(maps) and 0 <= dw[1] < len(maps[0]) and maps[dw[0]][dw[1]] == 1:
            dq.append([dw[0], dw[1], p[2] + 1])
            maps[dw[0]][dw[1]] = 0
    return -1

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])