# Valid Anagram
# two passes, hashmap tracks count of chars in str 1, decrement in str 2
# time: O(n), space: O(1) e.g. alphabet size
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort then compare, time: O(nlogn)
        # s = list(s).sort()
        # t = list(t).sort()
        # return s == t
        
        d = {} # tracks char counts
        for c in s:
            if d.get(c) is None:
                d[c] = 1
            else:
                d[c]+=1
        for c in t:
            if d.get(c) is None:
                return False
            else:
                d[c] -= 1
        for k,v in d.items():
            if v != 0:
                return False
        return True
