import math

N = int(input())
size = input().split()
size = list(map(int, size))
bulk_t, bulk_p = map(int, input().split())

order_t = [math.ceil(size[i] / bulk_t) for i in range(len(size))]
print(sum(order_t))
print(N // bulk_p, N % bulk_p)