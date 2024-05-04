def zero_subarray(nums):
    longest_subarray = 0
    for i in range(len(nums)):
        local_sum = nums[i]
        for j in range(i+1, len(nums)):
            local_sum += nums[j]
            if local_sum == 0:
                longest_subarray = max(longest_subarray,len(nums[i:j+1]))
    return longest_subarray