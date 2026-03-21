import sys
input = sys.stdin.readline

depth, width = map(int, input().strip("\n").split())
classroom = [[0] * width for _ in range(depth)]
start = list(map(int, input().strip("\n").split()))

rule_a = []
rule_b = []
for _ in range(depth):
    rule_a.append(input().strip("\n"))
for _ in range(depth):
    rule_b.append(input().strip("\n"))

movement = 0

while True:


    movement += 1
    if classroom[start[0]][start[1]] == 0:
        start[2] = (start[2] + int(rule_a[start[0]][start[1]])) % 4
        classroom[start[0]][start[1]] = 1
        answer = movement
        last_clean = [start[0], start[1], start[2]]
    else:
        start[2] = (start[2] + int(rule_b[start[0]][start[1]])) % 4
        if start == last_clean:
            print(answer)
            break

    if start[2] == 0:
        start[0] -= 1
        if start[0] < 0:
            print(answer)
            break
    elif start[2] == 1:
        start[1] += 1
        if start[1] >= width:
            print(answer)
            break
    elif start[2] == 2:
        start[0] += 1
        if start[0] >= depth:
            print(answer)
            break
    else:
        start[1] -= 1
        if start[1] < 0:
            print(answer)
            break

