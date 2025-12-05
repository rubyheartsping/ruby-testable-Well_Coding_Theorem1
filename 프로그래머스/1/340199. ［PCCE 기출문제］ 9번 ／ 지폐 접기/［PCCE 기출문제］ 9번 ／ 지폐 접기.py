import math

def solution(wallet, bill):
    answer = 0
    for x in range(8):
        while min(bill) > min(wallet) or max(bill) > max(wallet):
            if bill[0] > bill[1]:
                bill[0] = math.floor(bill[0] / 2)
            else:
                bill[1] = math.floor(bill[1] / 2)
            answer += 1

    return answer