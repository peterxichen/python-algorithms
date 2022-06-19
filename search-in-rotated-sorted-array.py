# Search in Rotated Sorted Array
# binary search, find which side is sorted or contains target
# time: O(logn), space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # binary search
        while l <= r:
            m = l + (r-l)//2 # midpoint
            if nums[m] == target:
                return m
            elif nums[m] < nums[l]: # right half is sorted
                if target > nums[m] and target <= nums[r]: # target in sorted half
                    l = m+1
                else: # target in non-sorted half
                    r = m-1
            else: # left half is sorted
                if target >= nums[l] and target < nums[m]: # target in sorted half
                    r = m-1
                else: # target in non-sorted half
                    l = m+1
        return -1 # not found
