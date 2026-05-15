def solution(k, ranges):
    
    traces = []
    while k != 1:
        traces.append(k)
        
        if k % 2 == 1:
            k = 3 * k + 1
        
        elif k % 2 == 0:
            k //= 2
    
    traces.append(1)
    
    areas = []
    for i in range(1, len(traces)):
        areas.append((traces[i] + traces[i-1]) / 2)
    
    prefix = [0]
    for i in range(len(areas)):
        prefix.append(prefix[-1] + areas[i])
    
    result = []
    for a, b in ranges:
        actual_b = len(traces) - 1 + b
        if a > actual_b:
            result.append(-1)
        else:
            result.append(prefix[b + len(prefix) - 1] - prefix[a])
        
    return result
        