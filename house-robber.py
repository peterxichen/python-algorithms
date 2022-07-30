# House Robber (cannot rob adjacent house, return max money can rob)
# init dp array = max robbed amount at nums[i:] (index i to end), 
# traverse in reverse, dp[i] = max(dp[i+1], dp[i+2] + nums[i]),
# robber 2 options: rob current house skip next OR rob next
# time: O(n), space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # empty case
        if not nums:
            return 0
        
        dp = [None for x in range(len(nums)+1)]
        # base case
        dp[len(nums)] = 0
        dp[len(nums)-1] = nums[len(nums)-1]
        
        for i in range(len(nums)-2, -1, -1): # traverse backwards
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        
        return dp[0]
