number, maximum = map(int, input().split())
cards = input().split()
cards = list(map(int, cards))
combos = []

for x in range(len(cards)):
    for y in range(x + 1, len(cards)):
        for z in range(y + 1, len(cards)):
            combos.append([cards[x], cards[y], cards[z]])

answer = []
for combo in combos:
    if sum(combo) <= maximum:
        answer.append(sum(combo))
    else:
        pass

print(max(answer))