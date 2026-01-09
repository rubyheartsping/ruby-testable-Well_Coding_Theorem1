from math import log
N = int(input())

for n in range(1, int(log(N, 2)) + 2):
    if 2 ** n > N:
        if 2 ** (n -1) == N:
            print(N)
            break
        else:
            print((N - (2 ** (n - 1))) * 2)