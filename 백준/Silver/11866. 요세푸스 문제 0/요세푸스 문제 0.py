N, K = map(int, input().split())
lst = [ordinal + 1 for ordinal in range(N)]
i = 0
answer = []
for n in range(N):
    i += K - 1
    i = i % len(lst)
    answer.append(str(lst[i]))
    lst.remove(lst[i])
print(f"<{", ".join(answer)}>")