import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        if "I" in operation:
            heapq.heappush(min_heap, int(operation[2:]))
            heapq.heappush(max_heap, -int(operation[2:]))
        elif operation == "D 1":
            if min_heap and max_heap:
                heapq.heappop(max_heap)
                min_heap.pop()
        else:
            if min_heap and max_heap:
                heapq.heappop(min_heap)
                max_heap.pop()
    return[-heapq.heappop(max_heap), heapq.heappop(min_heap)] if min_heap else [0, 0]
            
    
            