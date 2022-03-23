def solution(nums):
    set_num = set(nums)
    n = len(nums) // 2
    return len(set_num) if len(set_num) < n else n