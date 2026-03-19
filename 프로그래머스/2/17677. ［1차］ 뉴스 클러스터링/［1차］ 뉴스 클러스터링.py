from collections import Counter

def solution(str1, str2):
    list1 = [
        str1[i:i+2].lower()
        for i in range(len(str1) - 1)
        if str1[i:i+2].isalpha()
    ]
    list2 = [
        str2[i:i+2].lower()
        for i in range(len(str2) - 1)
        if str2[i:i+2].isalpha()
    ]

    counter1 = Counter(list1)
    counter2 = Counter(list2)

    inter = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())

    if union == 0:
        return 65536

    return int(inter / union * 65536)