X = int(input().split(" ")[1])
numbers = input().split(" ")

answer = []
for number in numbers:
    if int(number) < X:
        answer.append(number)
        
print(" ".join(answer))