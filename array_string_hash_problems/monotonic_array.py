def monotonicArr(arr):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            isNonDecreasing = False
        if arr[i] > arr[i-1]:
            isNonIncreasing = False
    return isNonIncreasing or isNonDecreasing