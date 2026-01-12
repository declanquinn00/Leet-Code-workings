def coinChange(self, coins: List[int], amount: int) -> int:
    # set an array slot for each value up to mount
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            # if we can take a coin from the amount
            if a - c >= 0:
                # the minimum is the current value it is or a previous value + a coin
                dp[a] = min(dp[a], 1 + dp[a - c])

                # return the correct amount excluding the additional value
    return dp[amount] if dp[amount] != amount + 1 else -1