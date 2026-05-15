from itertools import permutations

def solution(expression):
    number = ""
    arr = []
    for c in expression:
        if "0" <= c <= "9":
            number += c
        else:
            arr.append(int(number))
            arr.append(c)
            number = ""
    arr.append(int(number))
    
    def deep_copy(arr):
        arr_copy = []
        for element in arr:
            element_copy = element
            arr_copy.append(element_copy)
        return arr_copy
    
    nPr = permutations(["*", "-", "+"])
    operator_orders = list(nPr)
    candidate = []
    
    for operator_order in operator_orders:
        arr_copy = deep_copy(arr)
        for operator in operator_order:
            operator_count = arr_copy.count(operator)
            while operator_count != 0:
                idx = arr_copy.index(operator)
                if operator == "*":
                    arr_copy[idx-1] = arr_copy[idx-1] * arr_copy[idx+1]
                    arr_copy.pop(idx)
                    arr_copy.pop(idx)

                elif operator == "-":
                    arr_copy[idx-1] = arr_copy[idx-1] - arr_copy[idx+1]
                    arr_copy.pop(idx)
                    arr_copy.pop(idx)

                elif operator == "+":
                    arr_copy[idx-1] = arr_copy[idx-1] + arr_copy[idx+1]
                    arr_copy.pop(idx)
                    arr_copy.pop(idx)

                operator_count -= 1
        candidate.append(abs(arr_copy[-1]))
    return max(candidate)