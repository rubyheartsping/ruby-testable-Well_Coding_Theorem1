def solution(user_id, banned_id):
    answer = 0
    candidates = {i: set() for i in range(len(banned_id))}
    
    for i in range(len(banned_id)):
        for user in user_id:
            if len(banned_id[i]) == len(user):
                for j in range(len(banned_id[i])):
                    if banned_id[i][j] != "*" and banned_id[i][j] != user[j]:
                        break
                else:
                    candidates[i].add(user)
    print(candidates)
    
    result = set()
    
    def dfs(idx, selected):
        if idx == len(banned_id):
            result.add(tuple(sorted(selected)))
            return
        
        for user in candidates[idx]:
            if user not in selected:
                selected.add(user)
                dfs(idx + 1, selected)
                selected.remove(user)
    
    dfs(0, set())
    return len(result)        