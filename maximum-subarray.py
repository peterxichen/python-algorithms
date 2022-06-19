# Maximum Subarray
# single pass, running count of subarrray, start over if negative
# time: O(n), space: O(1) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0] # running count of subarray
        res = nums[0] # tracks max
        for i in range(1, len(nums)):
            # start over if subarray is negative
            cur = max(nums[i], cur + nums[i])
            res = max(cur, res)
        return res
