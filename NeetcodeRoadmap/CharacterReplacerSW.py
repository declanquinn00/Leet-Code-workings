def characterReplacement(s: str, k: int) -> int:
    r = l = 0
    window = {}
    max_window = 0

    for r in range(0, len(s)):
        # add to window first
        window[s[r]] = 1 + window.get(s[r], 0)
        max_val = max(window.values())
        #
        #    items = window.items()
        #    max_val = 0
        #    for key, val in items:
        #        max_val = max(val, max_val)
        #

        # while window size is over k
        # NEED TO HAVE THIS HERE BECAUSE SETTING TO A VARIABLE DIDN'T UPDATE IN WHILE LOOP!!!
        while (((r - l + 1) - max_val) > k):
            window[s[l]] = window[s[l]] - 1
            l += 1
            diff = ((r - l + 1) - max_val)
        max_window = max((r - l + 1), max_window)

    return max_window
s = "AAABABB"
k = 1

print(characterReplacement(s,k))