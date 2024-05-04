def max_of_k_subarray(nums, k):
    max_subarray = []
    max_val = float("-inf")
    for i in range(len(nums)-k+1):
        subarray = nums[i:i+k]
        cur_sum = sum(subarray)
        if cur_sum > max_val:
            max_val = cur_sum
            max_subarray = subarray[:]
    return max_subarray


s = [1,2,3,-12,5, 800]
print(max_of_k_subarray(s,3))