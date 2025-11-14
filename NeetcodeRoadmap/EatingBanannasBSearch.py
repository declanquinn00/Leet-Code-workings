import math
def minEatingSpeed(piles, h) -> int:
    # sort
    piles = sorted(piles)
    # get max eating rate = current rate # upper bound
    k = piles[len(piles) - 1]

    # compare the mid rate with the maxtime and current rate update if valid
    # Bin search
    l = 0
    r = piles[len(piles) - 1]
    # it will take at least this long at rate r

    min_rate = r

    while l <= r:
        dist = r - l
        mid = l + ((dist) // 2)
        rate = mid
        # get the time it takes to finish at this rate
        time = 0
        for i in range(0, len(piles)):
            time += math.ceil(float(piles[i]) / rate)
        if time <= h:
            r = mid - 1
            min_rate = mid
        else:
            l = mid + 1
    return min_rate

piles=[3,6,7,11]
h=8
print(minEatingSpeed(piles, h))