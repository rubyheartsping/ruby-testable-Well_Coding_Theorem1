def solution(n):
    binary = "0" + bin(n)[2:]
    len_binary = len(binary)
    count_0 = binary.count("0")
    count_1 = binary.count("1")
    multiplied_2 = set()
    m = 1
    while m <= 1_000_000:
        multiplied_2.add(m)
        m *= 2
    if len_binary == count_1:
        return (n + 1) * 1.5 - 1
    elif n in multiplied_2:
        return n
    else:
        for i in range(1, len_binary + 1):
            j = 1
            if binary[-i] == "1":
                while True:
                    if binary[-i-j] == "0":
                        new_binary = binary[:len_binary-(i + j)]
                        return int(new_binary + "1" + "0" * (count_0 - new_binary.count("0")) + "1" * (count_1 - new_binary.count("1") - 1), 2)
                    else:
                        j += 1
                