def trapping_rainwater(heights):
    maxLeft = 0
    maxRight = 0
    right = len(heights)-1
    left = 0
    total = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > maxLeft:
                maxLeft = heights[left]
            else:
                total += maxLeft - heights[left]
            left += 1
        else:
            if heights[right] > maxRight:
                maxRight = heights[right]
            else:
                total += maxRight - heights[right]
            right -= 1
    return total