# Container w/ Most Water
# 2 pointer each end, move shorter height toward middle
# time: O(n), space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointers on each end
        l, r = 0, len(height)-1
        cur_max = 0
        
        # move shorter height toward middle
        while l < r:
            l_height, r_height = height[l], height[r]
            cur_max = max(cur_max, min(l_height, r_height)*(r-l))
            if l_height < r_height:
                l+=1
            else:
                r-=1
        return cur_max
