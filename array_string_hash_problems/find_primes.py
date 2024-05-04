def find_primes(nums):
    res = []
    for num in nums:
        if num <= 0:
            continue
        elif num == 1:
            res.append(num)
            continue
        elif is_prime(num):
            res.append(num)
    return res

def is_prime(num):
    for i in range(2, num):
        if num % i == 0 or num == 2:
            return False
    return True