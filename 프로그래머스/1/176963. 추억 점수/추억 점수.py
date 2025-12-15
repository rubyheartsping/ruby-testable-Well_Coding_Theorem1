def solution(name, yearning, photo):
    for x in range(len(photo)):
        for y in range(len(photo[x])):
            if photo[x][y] in name:
                for n in range(len(name)):
                    if photo[x][y] == name[n]:
                        photo[x].remove(photo[x][y])
                        photo[x].insert(y, yearning[n])
                        break
                    else:
                        pass
            
            else:
                photo[x].remove(photo[x][y])
                photo[x].insert(y, 0)                
    answer = [sum(photo[i]) for i in range(len(photo))]
    return answer