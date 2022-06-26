# Minimum Window Substring
# sliding window, check if window contains all chars in t
# increase right pointer until match, then increase left pointer until not mathching
# Time/Space: O(len(s) + len(t))
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_size = float("inf") # tracks window substring size
        ans_l, ans_r = None, None # indices of answer in string s
        
        cnt_t = Counter(t) # k: char, v: count
        
        l, r = 0, 0 # 2 pointer tracking sliding window
        window = {} # counter of cur window in s (k: char, v: count)
        formed = 0 # tracks # chars in window w/ desired frequency
        
        # sliding window starting at index 0
        while r < len(s):
            # add char at "r" to window
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in cnt_t and window[s[r]] == cnt_t[s[r]]:
                formed+=1 # char matches desired frequency
                # don't +1 if > (skip duplicates)
            
            # while cur window has all chars (t is in window)
            while l <= r and formed == len(cnt_t):
                # save smallest window index until now
                if r-l+1 < ans_size:
                    ans_size = r-l+1
                    ans_l, ans_r = l,r
                
                # char at l no longer in window
                window[s[l]] -= 1
                if s[l] in cnt_t and window[s[l]] < cnt_t[s[l]]:
                    formed -= 1
                
                # move left pointer
                l += 1
            
            r +=  1 # move right pointer

        if ans_size == float("inf"):
            return "" # not found
        else:
            return s[ans_l: ans_r+1]
