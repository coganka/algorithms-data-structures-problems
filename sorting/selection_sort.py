def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        minChanged = False
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
                minChanged = True
        if minChanged:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr