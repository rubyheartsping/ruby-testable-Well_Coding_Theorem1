numbers = input().split(" ")
verification = 0
for num in numbers:
    verification += int(num) ** 2
    
print(str(verification)[-1:])
