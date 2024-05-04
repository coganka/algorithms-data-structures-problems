def find_second_largest(nums):
    nums = sorted(nums, reverse=True)
    for num in nums:
        if num != nums[0]:
            return num
    return None