# Palindromic Substrings
# helpmer method (2 pointer to count palindromes, middle out)
# do for each char in string
# time: O(n^2), space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalindrome(l, r):
            nonlocal cnt, s
            while (l>=0 and r<len(s) and s[l]==s[r]):
                cnt += 1
                l -= 1 # middle expand out 2 chars at a time
                r += 1        
        cnt = 0
        for i in range(len(s)):
            ispalindrome(i,i) # even pairs
            ispalindrome(i,i+1) # odd pairs
        return cnt
