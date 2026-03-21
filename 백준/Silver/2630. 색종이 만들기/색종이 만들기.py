import sys
input = sys.stdin.readline
white = 0
blue = 0
def inspect_divide(square, x, y, length):
    global white, blue
    first = square[x][y]
    same = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if square[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        if first == "0":
            white += 1
        else:
            blue += 1
        return
    
    half = length // 2
    inspect_divide(square, x, y, half)
    inspect_divide(square, x, y + half, half)
    inspect_divide(square, x + half, y, half)
    inspect_divide(square, x + half, y + half, half)


N = int(input())
square = [input().rstrip().split() for _ in range(N)]
inspect_divide(square, x = 0, y = 0, length = len(square))

print(white, blue)

