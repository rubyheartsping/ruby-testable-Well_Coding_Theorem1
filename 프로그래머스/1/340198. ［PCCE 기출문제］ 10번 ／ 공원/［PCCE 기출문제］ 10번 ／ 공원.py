def solution(mats, park):
    mats = sorted(mats)[::-1]
    for mat in mats:
        for m in range(len(park) - mat + 1):
            for n in range(len(park[m]) - mat + 1):
                inspector = []
                for i in range(mat):
                    for j in range(mat):
                        inspector.append(park[m + i][n + j])
            
                if inspector.count("-1") == mat ** 2:
                    return mat
        
    return -1
