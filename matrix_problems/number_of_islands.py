directions = [[0,1],[0,-1],[1,0],[-1,0]]

def number_of_islands(grid):
    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                island_count += 1
                traverse(grid, row, col)
    return island_count

def traverse(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    if grid[row][col] == "1":
        grid[row][col] = "0"
        for dir in directions:
            traverse(grid, row+dir[0], col+dir[1])
    return 