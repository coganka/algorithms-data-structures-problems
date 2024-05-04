def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right+left) // 2
        if nums[mid] == target:
            return (nums[mid],mid)
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None