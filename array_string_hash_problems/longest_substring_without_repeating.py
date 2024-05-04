def substr_without_repeating(s):
    if len(s) <= 1:
        return len(s)
    seen = {}
    left = 0
    longest = 0
    for right in range(len(s)):
        curChar = s[right]
        prevSeenChar = seen.get(curChar)
        if prevSeenChar != None and prevSeenChar >= left:
            left = prevSeenChar + 1
        seen[curChar] = right
        longest = max(longest, right - left + 1)
    return longest