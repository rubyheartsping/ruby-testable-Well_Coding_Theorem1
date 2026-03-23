from collections import deque

def solution(n, wires):
    answer = n

    for i in range(len(wires)):
        # 전선 하나 제거
        cut_wires = wires[:i] + wires[i+1:]

        # 그래프 만들기
        graph = [[] for _ in range(n + 1)]
        for a, b in cut_wires:
            graph[a].append(b)
            graph[b].append(a)

        # 1번 송전탑부터 BFS
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        count = 1

        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    count += 1

        answer = min(answer, abs(count - (n - count)))

    return answer