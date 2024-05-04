def twoSum(nums, target):
    hash = {}
    for i, num in enumerate(nums):
        if num in hash:
            return (hash[num],i)
        else:
            toFind = target - num
            hash[toFind] = i
    return None

s = [1,3,6,0,7,4]
print(twoSum(s,8))