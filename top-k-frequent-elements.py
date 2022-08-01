# Top K Frequent Elements
# create counter of nums, then either sort or create heap
# time: O(nlogk), spac: O(n+k) hashmap + heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # or Counter(nums), import from collections
        for i in nums: # create counts hashmap
            if not d.get(i):
                d[i] = 1
            else:
                d[i] += 1
        # if sorted into full list -> time: O(nlogn), space: O(n+n)
        # return [k for k,v in sorted(d.items(), key=lambda item: -item[1])][:k]
        # one line situation
        # return heapq.nlargest(k, d.keys(), key=d.get)
        
        # create heap
        from heapq import heappush, heappop
        h = []
        for key in d:
            # sorts by frequency (inverse for max heap)
            heappush(h, (-d[key], key))
        # pop k values
        res = []
        count = 0
        while count < k:
            frq, item = heappop(h)
            res.append(item)
            count+=1
        return res
