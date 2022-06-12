# binary search w/ 2 pointers
# time O(logN), space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1 or nums[r] > nums[0]:
            return nums[0] # already sorted
        while r>=l:
            mid = l + (r-l)//2 # integer div
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid+1 # min is right of mid
            else: # nums[mid] <= nums[0]
                r = mid-1 # min is left of mid
