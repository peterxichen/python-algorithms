# Longest Substring Without Repeating Characters
# single pass, sliding window, hashtable store index of last repeating char
# time: O(n), space O(min(string size, alphabet size))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {} # key: char, val: last index
        l, r = 0, 0
        longest = 0 # tracks result

        while r < len(s):
            # l = index of last appearing char (else 0)
            i = index.get(s[r])
            if i is not None and i>=l and i<r:
                l = i+1
            # max substring starting with "l"
            longest = max(longest, r-l+1)
            
            # store index and slide "r"
            index[s[r]] = r
            r += 1
        return longest
