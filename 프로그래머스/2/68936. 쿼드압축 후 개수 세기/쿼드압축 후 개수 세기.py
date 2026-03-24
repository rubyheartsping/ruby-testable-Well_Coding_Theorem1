

def solution(arr):
    zero = 0
    one = 0
    def inspect_divide(arr, x, y, length):
        nonlocal zero, one
        first = arr[x][y]
        same = True
        for i in range(x, x + length):
            for j in range(y, y + length):
                if arr[i][j] != first:
                    same = False
                    break
            if not same:
                break

        if same:
            if first == 0:
                zero += 1
            else:
                one += 1
            return

        half = length // 2
        inspect_divide(arr, x, y, half)
        inspect_divide(arr, x, y + half, half)
        inspect_divide(arr, x + half, y, half)
        inspect_divide(arr, x + half, y + half, half)
        
    inspect_divide(arr = arr, x = 0, y = 0, length = len(arr))
    return[zero, one]
        
        