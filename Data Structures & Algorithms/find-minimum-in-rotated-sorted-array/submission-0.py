class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        left = 0
        right = n-1
        res = float('inf')

        
        while left <= right:
            mid = (left+right) // 2 
            res = min(res,nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else: # nums[mid] < nums[right] means is sorted so we can free that part of the list
                right = mid - 1
        
        return res
        
        