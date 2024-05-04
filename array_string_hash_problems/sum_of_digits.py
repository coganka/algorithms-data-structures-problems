import math

def find_sum(nums):
    total = 0
    for num in nums:
        total += find_each(num)
    return total

def find_each(num):
    sumVal = 0
    while num > 0:
        digit = num % 10
        sumVal += digit
        num = math.floor(num / 10)
    return sumVal