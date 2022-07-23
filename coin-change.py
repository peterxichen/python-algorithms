# Coin Change (fewest # coins make up amount)
# subproblem: fewest amount needed ot build 1,2,3 .. etc
# dp array holds smallest amount of coins to make i mount
# dp[i] is fewest # of coins to make amount i, build up as needed
# time: O(coins * amount), space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i: # take coin if less than this amount
                    # current amount minus coin we just took
                    dp[i] = min(dp[i], 1+dp[i-coin])
                # else: break (coin needs to be sorted)
        return dp[-1] if dp[-1] != float('inf') else -1
