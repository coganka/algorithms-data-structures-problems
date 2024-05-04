#top-down approach
def fib_memo(n, lookup = None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        lookup[n] = fib_memo(n-1, lookup) + fib_memo(n-2, lookup)
        return lookup[n]
    
#bottom-up approach
def fib_tabu(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

#optimized bottom-up
def fib_opt_tabu(n):
    cur = 0
    before_prev = 0
    prev = 1
    for i in range(2, n+1):
        cur = prev + before_prev
        before_prev = prev
        prev = cur
    return prev