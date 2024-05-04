def remove_elements(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] == target:
            nums.pop(i)
        else:
            i+=1
    return nums