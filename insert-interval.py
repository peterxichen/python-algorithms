# Insert Interval
# greedy (pick locally optimal move), 3 cases:
# add intervals before newInterval, add newInterval, add intervals after newInterval
# time: O(n), space: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 # index
        n = len(intervals)
        output = []
        
        # case 1: add intervals before newInterval
        while i < n and newInterval[0] > intervals[i][0]:
            output.append(intervals[i])
            i += 1
        
        # case 2: add newInterval
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval) # no overlap
        else: # overlap, merge with newInterval
            output[-1][1] = max(output[-1][1], newInterval[1])

        # case 3: add intervals after newInterval
        while i < n:
            if output[-1][1] < intervals[i][0]:
                output.append(intervals[i]) # no overlap
            # if there is overlap, merge with last interval
            else:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            i += 1

        return output
