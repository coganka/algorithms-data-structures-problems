def odd_even(nums):
    longest = 0
    for i in range(len(nums)):
        local_long = 0
        odd_count, even_count = 0, 0
        for j in range(i, len(nums)):
            if nums[j] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            if even_count == odd_count:
                local_long += 1
        longest = max(longest, local_long)
    return longest * 2