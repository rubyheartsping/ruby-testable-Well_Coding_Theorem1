def solution(m, musicinfos):
    
    def time_extract(start, end):
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        time = (e_h - s_h) * 60 + (e_m - s_m)
        return time
    
    def remove_sharp(sound: str):
        sound = list(sound)
        for i in range(len(sound)):
            if sound[i] == "#":
                sound[i-1] = chr(ord(sound[i-1]) + 32)
        for _ in range(sound.count("#")):
            sound.remove("#")
        return "".join(sound)
    
    m = remove_sharp(m)
    candidate = []
    order = 0
    
    for musicinfo in musicinfos:
        start, end, title, sound = musicinfo.split(",")
        time = time_extract(start, end)
        sound = remove_sharp(sound)
        sound = sound * (time // len(sound)) + sound[:time % len(sound)]
        for i in range(len(sound) - len(m) + 1):
            if sound[i:i+len(m)] == m:
                candidate.append([time, -order, title])
                order += 1
                break
    candidate = sorted(candidate, reverse = True)
    return candidate[0][2] if candidate else "(None)"