# Word Break (if string can be segmented into dictionary words)
# dp array of len(s) where dp[i] = True if can be segmented
# nested loop to traverse, if at any point the inner loop s[0:j]==True
# and remaining substring (until end s[j:end]) is in word dict then mark True
# time: O(n^3), O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict) # for constant lookup
        dp = [False] * (len(s)+1)
        dp[0] = True # initialize
        
        for i in range(1, len(s)+1):
            for j in range(i):
                # s[0:j] can be segmented + s[j:end] is a word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[-1]
