def solution(n, arr1, arr2):
    return [
        format(arr1[i] | arr2[i], f"0{n}b")
        .replace("1", "#")
        .replace("0", " ")
        for i in range(n)
        
    ]