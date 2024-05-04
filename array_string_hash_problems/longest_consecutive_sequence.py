def consecutive(nums):
    longest = 1
    curlongest = 1
    for i in range(len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            curlongest += 1
        else:
            curlongest = 1
        longest = max(longest, curlongest)
    return longest