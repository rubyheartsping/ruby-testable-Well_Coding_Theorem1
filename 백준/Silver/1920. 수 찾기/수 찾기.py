import sys
input = sys.stdin.readline
N = int(input())
lst1 = set(input().rstrip("\n").split())
M = int(input())
lst2 = input().rstrip("\n").split()

for i in range(M):
    if lst2[i] in lst1:
        print(1)
    else:
        print(0)