def solution(nums):
    halfnums = len(nums) / 2
    nums = set(nums)
    if len(nums) >= halfnums:
        return halfnums
    
    else:
        return len(nums)