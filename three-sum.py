# 3 Sum
# Option 1) sort, single pass use 2sum helper method w/ 2 pointers
# Option 2) no sorting, double loop, store complement (3rd element) in hashmap
# time O(n^2), space O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting array
        nums.sort() # nlogn
        result = []
        
        def twoSum(nums, i, result):
            # find 3sum w/ i included in triplet
            l, r = i+1, len(nums)-1 # 2 pointers
            while l < r:
                this_sum = nums[i] + nums[l] + nums[r]
                if this_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
                elif this_sum < 0:
                    l += 1
                elif this_sum > 0:
                    r -= 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break # rest cannot sum to zero
            # skip duplicates (unique triplets)
            if i==0 or nums[i-1] != nums[i]:
                twoSum(nums, i, result)
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set() # tracks duplicate values
        seen = {} # key: nums[j], val: i

        for i in range(len(nums)):
            if nums[i] not in dups: # skip duplicates
                dups.add(nums[i])
                for j in range(i+1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    seen[nums[j]] = i # store in hashmap
        return res
