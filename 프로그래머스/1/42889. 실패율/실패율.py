from collections import Counter

def solution(N, stages):
    stages = Counter(stages)
    number = sum(list(stages.values()))
    stages = sorted(stages.items(), key=lambda x: x[0])
    fail_ratio = {i + 1 : 0 for i in range(N)}
    for stage in stages:
        fail_ratio.update({stage[0] : stage[1] / number})
        number -= stage[1]
    if N not in fail_ratio.keys():
        fail_ratio.update({N : 0})
    fail_ratio.pop(N + 1, "None")
    fail_ratio = sorted(fail_ratio.items(), key = lambda x : x[1], reverse = True)
    fail_ratio = [x[0] for x in fail_ratio]
    return fail_ratio