from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    words.append(begin)
    graph = {word : [] for word in words}
    visited = {word : False for word in words}
    print(visited)
    while words:
        candidate = words.pop()
        for word in words:
            counter = 0
            for i in range(len(begin)):
                if candidate[i] != word[i]:
                    counter += 1
            if counter == 1:
                graph[candidate].append(word)
                graph[word].append(candidate)
    
    words = list(graph.keys())
    dq = deque([words.pop()])
    visited[begin] = True
    count = 0
    while dq:
        cur = dq.popleft()
        if cur == target:
            return count
        for word in words:
            if cur in graph[word] and visited[word] == False:
                dq.append(word)
                visited[word] = True
        count += 1
        