def spiralTraverse(matrix):
    res = []
    helper(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, res)
    return res

def helper(matrix, startRow, endRow, startCol, endCol, res):
    if startRow > endRow or startCol > endCol:
        return
    for col in range(startCol, endCol+1):
        res.append(matrix[startRow][col])
    for row in range(startRow+1, endRow+1):
        res.append(matrix[row][endCol])
    for col in reversed(range(startCol, endCol)):
        res.append(matrix[endRow][col])
    for row in reversed(range(startRow+1, endRow)):
        res.append(matrix[row][startCol])
    helper(matrix, startRow+1, endRow-1, startCol+1, endCol-1, res)