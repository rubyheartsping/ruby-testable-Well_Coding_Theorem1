N = int(input())
numbers = input().split()
numbers = list(map(int, numbers))
print(min(numbers), max(numbers))