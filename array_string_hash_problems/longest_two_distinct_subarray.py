def longest_2_subarray(nums):
    if len(nums) <= 1:
        return len(nums)
    max_length = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            subarray = nums[i:j+1]
            if len(set(subarray)) <= 2:
                length = len(subarray)
                max_length = max(max_length, length)
            else:
                break
    return max_length

s = [1]
print(longest_2_subarray(s))