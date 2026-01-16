N, M = map(int, input().split())
board = [str(input()) for n in range(N)]

ideal = "WB" * 32
candidate = []
for n in range(N - 7):
    for m in range(M - 7):
        inspector = ""
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    inspector += board[n + i][m + j]
                else:
                    inspector += board[n + i][m - j + 7]
        
        real = 0
        for k in range(64):
            if inspector[k] != ideal[k]:
                real += 1
        
        real = min(real, 64 - real)
        candidate.append(real)

print(min(candidate))