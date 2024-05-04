#top-down approach
def rob_memo(arr, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    if i >= len(arr):
        return 0
    else:
        lookup[i] = max(arr[i] + rob_memo(arr, i+2, lookup), rob_memo(arr, i+1, lookup))
        return lookup[i]
    
#bottom-up approach
def rob_tabu(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    return dp[n-1]