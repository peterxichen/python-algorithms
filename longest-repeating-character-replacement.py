# Longest Repeating Character Replacement
# single pass sliding window, check if substring minus most repeated
# characters is above k (shorten string if so)
# time: O(n), space: O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} # tracks frequency of each char in substr
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            freq[c] = 0
        
        l, r = 0, 0 # sliding window pointers
        max_len = 0
        most_repeated = 0
        
        while r < len(s): # substr: l->r
            freq[s[r]] += 1 # track frequency in subtr
            most_repeated = max(most_repeated, freq[s[r]])
            
            # substr minus most repeated > k
            if r-l-most_repeated+1 > k:
                # shorten substr if > k
                freq[s[l]] -= 1
                l += 1
            
            # track length of substr
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len
