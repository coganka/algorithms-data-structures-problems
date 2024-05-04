def largest_increase(nums):
    maxlen = 0
    for i in range(len(nums)):
        cur_len = 1
        for j in range(i+1, len(nums)):
            if nums[j] > nums[j-1]:
                cur_len += 1
            else:
                break
        maxlen = max(maxlen, cur_len)
    return maxlen