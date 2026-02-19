def solution(data, ext, val_ext, sort_by):
    answer = []
    formation = ["code", "date", "maximum", "remain"]
    ext = formation.index(ext)
    sort_by = formation.index(sort_by)
    for d in data:
        if d[ext] < val_ext:
            answer.append(d)
    return sorted(answer, key = lambda x : x[sort_by])