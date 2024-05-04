def quickSort(arr):
    if len(arr) <= 1:
        return arr
    quick(arr, 0, len(arr)-1)
    return arr

def quick(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if (arr[left] >= arr[pivot] and arr[right] <= arr[pivot]):
            arr[left], arr[right] = arr[right], arr[left]
        if (arr[left] <= arr[pivot]):
            left += 1
        if (arr[right] >= arr[pivot]):
            right -= 1
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick(arr, start, right-1)
    quick(arr, right+1, end)
    return