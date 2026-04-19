class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) -1
        i = 0
        maxArea = 0

        while i <= j:
            width = (j-i)
            height = min(heights[i],heights[j])
            maxArea = max(width * height, maxArea)

            if heights[i] >= heights[j]:
                j-=1
            else:
                i +=1

            
        
        print(maxArea)

        return maxArea




        