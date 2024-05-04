def longest_pal_substr(st):
    max_count = 0
    for i in range(len(st)):
        count = 0
        right = len(st)-1
        left = i
        while st[left] != st[right]:
            right -= 1
        while left <= right:
            if st[left] != st[right]:
                break
            else:
                count = count + 1 if left == right else count + 2
                right -= 1
                left += 1
        max_count = max(max_count, count)
    return max_count