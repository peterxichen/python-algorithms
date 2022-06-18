# Maximum Product Subarray
# single pass, track max/min thus far
# time: O(n), space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # track min/max products thus far
        max_so_far = nums[0]
        min_so_far = nums[0] # handle negative
        res = max_so_far

        # only zeroes or negatives disrupt positives
        for i in range(1, len(nums)):
            cur = nums[i]
            cur_x_min = cur * min_so_far
            cur_x_max = cur * max_so_far
            
            # cur handles zeroes, min handles neg
            min_so_far = min(cur, cur_x_min, cur_x_max)
            max_so_far = max(cur, cur_x_min, cur_x_max)
            
            res = max(res, max_so_far)
        return res
