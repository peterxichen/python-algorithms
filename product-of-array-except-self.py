# product of array except self
# 1st pass left to right, 2nd pass in reverse
# time: O(n), space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)): # product of elements to left
            ans[i] = nums[i-1]*ans[i-1]
        temp = 1 # product of all elements to right
        for i in reversed(range(len(nums))):
            ans[i] = ans[i]*temp
            temp *= nums[i]
        return ans
