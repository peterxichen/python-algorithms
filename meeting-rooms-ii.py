# Meeting Rooms II
# sort by start time, iter through times append to heap,
# put end times into min heap, top/min room frees earliest,
# pop top room if free (< cur start time)
# time: O(nlogn), space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = [] # minheap/priortiy queue w/ end times
        intervals.sort(key=lambda x: x[0]) # sort by start time
        heapq.heappush(rooms, intervals[0][1]) # add 1st meeting
        for i in intervals[1:]: # remaining meetings
            # top (min) room frees earliest
            if rooms[0] <= i[0]: # room is freed up
                heapq.heappop(rooms) # logN, remove min
            heapq.heappush(rooms, i[1])
        return len(rooms) # rooms = final end time of each room
