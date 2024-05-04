def maxArea(heights):
    left = 0
    right = len(heights)-1
    mxArea = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        mxArea = max(area, mxArea)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return mxArea