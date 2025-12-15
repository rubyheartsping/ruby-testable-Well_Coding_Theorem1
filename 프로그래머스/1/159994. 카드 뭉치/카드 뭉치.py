def solution(cards1, cards2, goal):
    count1 = 0
    count2 = 0
    for i in range(len(goal)):
        if count1 < len(cards1) and cards1[count1] == goal[i]:
            count1 += 1
            
        elif count2 < len(cards2) and cards2[count2] == goal[i]:
            count2 += 1
            
        else:
            return "No"
    return "Yes"