from collections import Counter

def solution(genres, plays):
    dict_count = {genre : [[], 0] for genre in set(genres)}
    for i in range(len(genres)):
        dict_count[genres[i]][0].append([plays[i], i])
        dict_count[genres[i]][1] += plays[i]
    print(dict_count.items())
    popular_genres = [genre for genre in dict_count.keys()]
    popular_genres = sorted(popular_genres, key = lambda x : dict_count[x][1], reverse = True)
    answer = []
    for genre in popular_genres:
        dict_count[genre][0] = sorted(dict_count[genre][0], key = lambda x : x[0], reverse = True)
        answer.append(dict_count[genre][0][0][1])
        if len(dict_count[genre][0]) >= 2:
            answer.append(dict_count[genre][0][1][1])
    return answer
    