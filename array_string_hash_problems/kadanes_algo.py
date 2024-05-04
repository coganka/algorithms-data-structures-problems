def kadane(arr):
    localSum = arr[0]
    globalSum = arr[0]
    for num in arr[1:]:
        localSum = max(num, localSum + num)
        globalSum = max(localSum, globalSum)
    return globalSum