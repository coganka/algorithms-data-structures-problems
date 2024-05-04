def remove_duplicate_1(nums):
    return list(set(nums))

def remove_duplicate_2(nums):
    seen = set()
    res = []
    for num in nums:
        if num not in seen:
            res.append(num)
        seen.add(num)
    return res