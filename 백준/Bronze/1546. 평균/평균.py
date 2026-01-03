subjects = int(input())
scores = input().split()
scores = list(map(int, scores))
answer = []
for i in scores:
    answer.append(i / max(scores) * 100)
print(sum(answer) / len(answer))