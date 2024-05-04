def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    leftIdx, rightIdx = 0, 0
    res = []
    while leftIdx < len(left) and rightIdx < len(right):
        if (left[leftIdx] < right[rightIdx]):
            res.append(left[leftIdx])
            leftIdx += 1
        else:
            res.append(right[rightIdx])
            rightIdx += 1
    return res + left[leftIdx:] + right[rightIdx:]