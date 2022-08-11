def climbStairs(self, n):
    tmp = int(n)
    if tmp == 1:
        return tmp
    if tmp == 2:
        return tmp

    prev = 1
    cur = 2

    for i in range(3, tmp + 1):
        total = prev + cur
        prev = cur
        cur = total
    return cur