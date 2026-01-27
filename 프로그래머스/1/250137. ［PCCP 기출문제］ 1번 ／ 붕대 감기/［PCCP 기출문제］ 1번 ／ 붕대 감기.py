def solution(bandage, health, attacks):
    time = 0
    success = 0
    i = 0
    current_health = health
    for _ in range(attacks[-1][0]):
        time += 1
        success += 1
        if time == attacks[i][0]:
            current_health -= attacks[i][1]
            i += 1
            if i > len(attacks):
                i = 0
            success = 0
            if current_health <= 0:
                return -1
        
        else:
            current_health += bandage[1]
            if success == bandage[0]:
                current_health += bandage[2]
                success = 0
            
            if current_health > health:
                current_health = health
    
    return current_health