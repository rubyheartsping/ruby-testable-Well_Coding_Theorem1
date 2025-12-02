def solution(s):
    answer = s.split(" ")

    for i in range(len(answer)):
        answer[i] = list(answer[i])

    for x in range(len(answer)):
        for y in range(len(answer[x])):
            if y % 2 == 0:
                answer[x][y] = answer[x][y].upper()
            if y % 2 == 1:
                answer[x][y] = answer[x][y].lower()
    
    answer1 = ""
    for row in range(len(answer)):
        if row == 0:
            answer1 += "".join(answer[row])
        else:
            answer1 = answer1 + " " + "".join(answer[row])

    return answer1