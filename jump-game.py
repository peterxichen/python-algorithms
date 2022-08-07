# Jump Game
# greedy, init variable to track position, traverse list in reverse,
# if i + nums[i] greater than position then move position to i,
# at end of traversal check if position is at 0
# time: O(n), space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums)-1
        # traverse indices in reverse
        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i] >= last_pos):
                last_pos = i
        return last_pos == 0
