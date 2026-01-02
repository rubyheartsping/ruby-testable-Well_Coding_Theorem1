N = int(input())

for i in range(1, N + 1):
    stars = [" " for j in range(N - i)]
    for k in range(i):
        stars.append("*")
            
    print("".join(stars))