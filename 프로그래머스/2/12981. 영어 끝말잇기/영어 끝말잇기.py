def solution(n, words):
    inspector = set()
    inspector.add(words[0])
    for i in range(1, len(words)):
        if words[i - 1][-1] == words[i][0] and words[i] not in inspector:
            inspector.add(words[i])
        else:
            num_people = (i + 1) % n if (i + 1) % n != 0 else n
            num_order = ((i + 1) // n) + 1 if (i + 1) % n != 0 else (i + 1) // n
            return [num_people, num_order]
    
    return [0, 0]