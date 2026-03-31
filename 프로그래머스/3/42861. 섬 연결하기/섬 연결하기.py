def solution(n, costs):
    answer = 0
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        rootA = find(parent, a)
        rootB = find(parent, b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            
    parent = [num for num in range(n)]
    costs = sorted(costs, key = lambda x : x[2])
    
    for a, b, cost in costs:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    
    return answer
    