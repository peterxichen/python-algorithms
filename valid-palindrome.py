# Valid Palindrome
# two pointers at each end, move to middle
# time O(n), space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(lambda c: c.isalnum(), s)
        s = map(lambda c: c.lower(), s)
        s = list(s)
        
        # space O(n)
        # return s[::-1] == s 
        
        i, j = 0, len(s)-1 # two pointers
        while i < j:
            # not needed if already converted
            # while i < j and not s[i].isalnum():
            #    i += 1
            # while i < j and not s[j].isalnum():
            #    j -= 1
            if s[i] != s[j]: # .islower() not needed if converted
                return False
            i+=1
            j-=1
        return True
