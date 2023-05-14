def isPalindrome(s):
    s = s.replace(" ", "")
    s = list(s)
    s2 = []
    if len(s) == 0:
        return True
    for i in range(0, len(s)):
        if ord(s[i]) <= 90 and ord(s[i]) >= 65:
            order = ord(s[i]) + 32
            s2.append(chr(order))
        elif (ord(s[i]) >= 97 and ord(s[i]) <= 122) or  (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            s2.append(s[i])

    halfPlusOne = int((len(s2) / 2) + 1)

    for j in range(0, halfPlusOne):
        if s2[j] != s2[(len(s2)-1) - j]:
            return False

    return True

s = "racecar a racecar"
s2 = "racecar; a racecar"
s3 = "racecar; a racecar0"

isPalindrome(s3)