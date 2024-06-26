def rotateImage(matrix):
    l = 0
    r = len(matrix[0])
    while l < r:
        for i in range(r-l):
            top, bottom = l, r
            topLeft = matrix[top][l+i]

            matrix[top][l+i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r-i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = topLeft
        l+=1
        r-=1
    return matrix