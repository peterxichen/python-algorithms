# Merge Intervals
# sort by first element, traverse to append interval or update right bound
# time: O(nlogn), space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort (heapsort ~ologn)
        merged = []
        for i in intervals:
            # case 1: prev max < next min, append new interval
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            # case 2: prev max >= next min, update prev max to equal bigger max
            else:
                merged[-1][1] = max(i[1], merged[-1][1])
        return merged
