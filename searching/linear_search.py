def linear_search(nums, target):
    for i,num in enumerate(nums):
        if num == target:
            return (num,i)
    return None