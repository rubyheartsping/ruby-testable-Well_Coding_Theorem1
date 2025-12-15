def solution(number, limit, power):
    steel = []
    for n in range(1, number + 1):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):    
            if n % i == 0:
                result.add(i)
                result.add(n // i)

        if len(result) <= limit:
            steel.append(len(result))
        else:
            steel.append(power)
    return sum(steel)