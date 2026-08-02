def solution(nums):
    unique_types = set(nums)
    max_pick = len(nums) // 2
    
    if len(unique_types) > max_pick:
        return max_pick
    else:
        return len(unique_types)