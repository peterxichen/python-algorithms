# Group Anagrams
# create HashMap (k: counter of each char, v: list of string)
# time/space: O(number of strings)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        ans = {} # k: count of each char, v: list of string
        for s in strs:
            d = {} # k: alphabet, v: counter
            for x in alphabet:
                d[x] = 0 # initialize
            for c in s:
                d[c] += 1
            key = str(d) # encode dict as string
            
            # insert into ans
            if ans.get(key):
                ans[key].append(s)
            else:
                ans[key] = [s]
        return ans.values()
