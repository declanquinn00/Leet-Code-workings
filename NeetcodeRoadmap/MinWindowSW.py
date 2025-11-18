def minWindow(s: str, t: str) -> str:
    # check s>t
    if len(s) < len(t):
        return ""

    check = {}
    window = {}
    have = 0
    need = len(t)
    max_size = len(s)
    l = 0
    max_l = 0
    max_r = 0

    # fill out the check map
    for char in t:
        check[char] = 1 + check.get(char, 0)

    for r in range(0, len(s)):
        # add to window
        window[s[r]] = 1 + window.get(s[r], 0)
        if s[r] in check:
            val = window[s[r]]
            if val <= check[s[r]]:
                have += 1

        while have == need and l <= r:
            # get window length
            size = r - l + 1
            if size <= max_size:
                max_size = size
                max_l = l
                max_r = r

            # remove left
            window[s[l]] = window.get(s[l], 0) - 1
            if s[l] in check:
                if window[s[l]] < check[s[l]]:
                    have -= 1
            if window[s[l]] <= 0:
                window.pop(s[l])
            l = l + 1


    return s[max_l:max_r + 1]

s = "UZODYXAZV"
t = "XYZ"
print(minWindow(s,t))