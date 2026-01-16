import sys
input = sys.stdin.readline

def check(x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)
S = set()
M = int(input())
for m in range(M):
    command = str(input().rstrip("\n"))
    if command[0:3] == "add":
        S.add(int(command[4:]))

    elif command[0] == "r":
        if int(command[7:]) in S:
            S.remove(int(command[7:]))
    
    elif command[0] == "c":
        check(int(command[6:]))
    
    elif command[0] == "t":
        toggle(int(command[7:]))
    
    elif command[0] == "a":
        S = {i for i in range(1, 21)}
    
    elif command[0] == "e":
        S = set()


