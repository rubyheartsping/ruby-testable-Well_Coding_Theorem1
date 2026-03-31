import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a
    
N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union(parent, i + 1, j + 1)
    
checklist = list(map(int, input().split()))
for check in range(len(checklist)-1):
    if find(parent, checklist[check]) != find(parent, checklist[check+1]):
        print("NO")
        break
else:
    print("YES")
            
    