import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for n in range(N)]
numbers = sorted(numbers)
for number in numbers:
    print(number)