n = 3
def sol(n):
    counter = 0
    while n != 0:
        if n & 1:
            counter += 1
        n = n >> 1

    return counter

count = sol(n)