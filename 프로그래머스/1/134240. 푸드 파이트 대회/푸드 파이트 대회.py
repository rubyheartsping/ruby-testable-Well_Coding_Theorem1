def solution(food):
    result = []
    for x in range(1, len(food)):
        if food[x] % 2 == 0:
            result.append(str(int((x)))*int((int(food[x]) / 2)))

        elif food[x] % 2 == 1:
            result.append(str(int((x)))*int((int(food[x] - 1) / 2)))

    return ("".join(result) + "0" + "".join(result)[::-1])
