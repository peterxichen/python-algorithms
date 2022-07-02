# Meeting Rooms
# sort by start time, compare if end time > start time of next meeting
# traverse through all meetings, if yes then conflict
# time: O(nlogn), space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0]) # heapsort O(nlogn) time O(1) space
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
