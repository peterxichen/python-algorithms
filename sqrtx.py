# Square Root e.g. Sqrt(x)
# binary search, 2 pointer, half interval until midpoint^2 equals x
# time: O(logN), space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 2, x//2 # 2 pointer, interval
        
        while l <= r:
            pivot = l + (r-l)//2 # midpoint
            num = pivot * pivot
            if num > x: # move right boundary left
                r = pivot-1
            elif num < x: # move left boundary right
                l = pivot+1
            else: # x = piv^2 -> sqrt found 
                return pivot
        return r
