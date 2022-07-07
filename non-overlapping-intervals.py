# Non-overlapping Intervals
# sort by end value, iterate through intervals, greedy (local optimized):
# case 1: no overlap, case 2: start of next before end of previous
# time: O(nlogn), space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1]) # sort by end (nlogn)

        this_end = intervals[0][1] # track nonoverlapping end
        count = 0

        # case 1: no overlap
        # case 2: start of next before end of previous
        for i in range(1, len(intervals)):
            if intervals[i][0] >= this_end: # case 1
                this_end = intervals[i][1]
            else: # case 2, drop current interval
                count += 1
        return count
