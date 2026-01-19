import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().rstrip().split()))

prefix = [0] * (N + 1)

for i in range(N):
    prefix[i+1] = prefix[i] + numbers[i]

for _ in range(M):
    i, j = map(int, input().rstrip("\n").split())
    print(prefix[j] - prefix[i - 1])
