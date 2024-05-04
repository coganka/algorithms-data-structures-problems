def abs_diff(nums):
    total = 0
    for i in range(len(nums)-1):
        total += abs(nums[i] - nums[i+1])
    return total