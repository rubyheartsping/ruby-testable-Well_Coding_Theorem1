import sys
# input = sys.stdin.readline

N = int(input().rstrip("\n"))
connections = int(input().rstrip("\n"))
dict_conn = {f"{i}" : set() for i in range(1, N + 1)}
for connection in range(connections):
    computer1, computer2 = map(str, input().rstrip("\n").split())
    dict_conn[computer1].add(computer2)
    dict_conn[computer2].add(computer1)

infected = set(dict_conn["1"]) | {"1"}  # 시작 감염(1 포함)

while True:
    new_infected = set(infected)
    for c in infected:
        new_infected |= dict_conn[c]
    if new_infected == infected:
        break
    infected = new_infected
    
if len(infected) != 0:
    print(len(infected) - 1)
else:
    print(0)