# Longest Palindromic Substring
# helper method middle out 2 pointer check palindrome
# loop through string, call helper
# time: O(n^2), space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 0
        longest_str = ""
        def isPal(l,r):
            nonlocal longest_str, longest_len, s
            while (l>=0 and r<len(s) and s[l]==s[r]):
                substr = s[l:r+1]
                if len(substr) > longest_len:
                    longest_len = len(substr)
                    longest_str = substr
                l -= 1
                r += 1
        for i in range(len(s)):
            isPal(i,i)
            isPal(i,i+1) # pointers 2 chars per iter
        return longest_str
