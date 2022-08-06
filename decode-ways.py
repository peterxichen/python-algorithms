# Decode Ways
# dp[i] = num ways of decoding substring s[:i]
# dp[i] = dp[i-1] + dp[i-2] when decode is possible
# if s[i-1] single digit -> add dp[i-1]
# if s[i-2]+s[i-1] double digit -> add dp[i-2]
# time: O(n), space: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        # array to store subproblem
        dp = [0 for i in range(len(s)+1)]
        
        # initialize
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        # store in dp[i] for substring s[i-2] + s[i-1]
        for i in range(2, len(dp)):
            # single digit decode possible
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # two digit decode possible
            if int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]

        return dp[-1]