# House Robber II (houses arranged in circle, cannot rob adjacent, return max money)
# implement house robber I as helper -> return max(helper[:-1], helper[1:])
# time: O(n), space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0 or nums is None:
            return 0
        if len(nums)==1:
            return nums[0]
        
        def helper(nums): # house robber 1
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

        return max(helper(nums[:-1]), helper(nums[1:]))
