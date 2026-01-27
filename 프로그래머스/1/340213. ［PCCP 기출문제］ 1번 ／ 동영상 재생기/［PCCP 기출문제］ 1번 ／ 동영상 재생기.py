def to_sec(time):
    return int(time[0:2]) * 60 + int(time[3:])

def to_minsec(time):
    return f"{time // 60:02d}:{time % 60:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    if (pos >= op_start) and (pos <= op_end):
        pos = op_end

    for command in commands:
        if command == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
            if (pos >= op_start) and (pos <= op_end):
                pos = op_end
        
        elif command == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
            if (pos >= op_start) and (pos <= op_end):
                pos = op_end
    
    return to_minsec(pos)
