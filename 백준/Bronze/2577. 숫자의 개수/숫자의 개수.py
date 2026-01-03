A = int(input())
B = int(input())
C = int(input())

multi = A * B * C
for i in range(10):
    try:
        print(str(multi).count(str(i)))
    except ValueError:
        print(0)