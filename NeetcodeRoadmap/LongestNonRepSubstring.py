def lengthOfLongestSubstring( s: str) -> int:
    i = 0
    j = 0
    curr_max = 0
    chars = set()
    for i in range(0, len(s)):
        while j < len(s) and s[j] not in chars:
            chars.add(s[j])
            diff = j+1 - i
            curr_max = max(curr_max, diff)
            j += 1

        if j < len(s) and s[j] in chars:
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
    return curr_max

s = "abcabcbb"
lengthOfLongestSubstring(s)