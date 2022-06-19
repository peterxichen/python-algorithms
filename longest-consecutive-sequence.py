# Longest Consecutive Sequence
# put array into hash set, single pass through hash set, check for neighbors
# time: O(n), space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Set (key no value, O(1) lookup)
        numset = set(nums)
        streak = 0
        for num in numset:
            # start count only if start of sequence
            if num-1 not in numset:
                cur = num
                this_streak = 1
                while cur+1 in numset:
                    cur += 1
                    this_streak += 1
                streak = max(streak, this_streak)
        return streak
