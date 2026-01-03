word = input()
alphabet = [chr(i) for i in range(97, 123)]
answer = {}
for alpha in alphabet:
    answer.update({alpha : "-1"})
for idx, i in enumerate(word):
    if answer[i] == "-1":
        answer.update({i : str(idx)})
    
print(" ".join(list(answer.values())))