class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        leftmax = 0
        rightmax = 0
        rain_water = 0

        while left < right:
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])
            
            # left is is smaller
            if leftmax < rightmax:
                rain_water += leftmax - height[left]
                left += 1
            #right is smaller
            else:
                rain_water += rightmax - height[right]
                right -=1         

        return rain_water
        