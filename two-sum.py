# hash table stores complement (target minus index), single pass
# time: O(n), space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            this = d.get(nums[i])
            if this is not None:
                return [this, i]
            d[target - nums[i]] = i
