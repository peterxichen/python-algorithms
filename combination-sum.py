# Combination Sum (num possible combinations that add up to target)
# init dp array where d[i] is the num combinations that sum up to value i,
# for each num value, if i-num>=0 then add to dp[i] existing combinations stored at dp[i-num]
# time: O(target value * num elements), space: O(num elements)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums.sort() (optimization)
        dp = [0 for i in range(target+1)]
        dp[0] = 1 # base case
        
        for i in range(target+1):
            for num in nums:
                if i - num >= 0:
                    # add existing combinations (or 1 if i==n)
                    dp[i] += dp[i-num]
                # else: break (optimization)
        return dp[-1]
