from collections import Counter

N = int(input())
lst1 = input().split()
M = int(input())
lst2 = input().split()

freq = Counter(lst1)  # O(N)

answer = [str(freq[x]) for x in lst2]  # 각 조회 O(1) 평균
print(" ".join(answer))