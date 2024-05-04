def majorityElement(nums):
    if len(nums) < 1:
        return None
    hash = {}
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    maxNum = 0
    elem = 0
    for key in hash:
        if hash[key] > maxNum:
            maxNum = hash[key]
            elem = key
    return elem