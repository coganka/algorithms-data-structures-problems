def max_sum(nums):
    maxsum = float("-inf")
    for i in range(len(nums)):
        p1, p2 = 0, 1
        while p2 < len(nums) - 1:
            if p2 == i:
                p2 += 1
            if p1 == i:
                p1 += 1
            sum = nums[i] * nums[p1] * nums[p2]
            maxsum = max(maxsum, sum)
            p1 += 1
            p2 += 1
    return maxsum

s = []
print(max_sum(s))
        