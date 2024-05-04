from functools import reduce

def find_max(nums):
    if len(nums) < 3:
        return False
    sorted_nums = sorted(nums, reverse=True)
    return reduce(lambda x,y: x * y, sorted_nums[:3], 1)