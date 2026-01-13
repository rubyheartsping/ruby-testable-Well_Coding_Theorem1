import sys
input = sys.stdin.readline

def push(lst: list, x):
    lst.append(x)

def pop_x(lst):
    if len(lst) != 0:
        print(lst[0])
        lst.remove(lst[0])
    else:
        print(-1)

def size(lst):
    print(len(lst))

def empty(lst):
    if len(lst) != 0:
        print(0)
    else:
        print(1)

def front(lst):
    if len(lst) != 0:
        print(lst[0])
    else:
        print(-1)

def back(lst):
    if len(lst) != 0:
        print(lst[len(lst) - 1])
    else:
        print(-1)

N = int(input().rstrip("\n"))
lst = []
for n in range(N):
    command = str(input().rstrip("\n"))
    if "push" in command:
        x = command.split()[1]
        push(lst, x)
    elif command == "pop":
        pop_x(lst)
    elif command == "size":
        size(lst)
    elif command == "empty":
        empty(lst)     
    elif command == "front":
        front(lst)
    elif command == "back":
        back(lst)
