class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left and right products
        n = len(nums)
        ans = [0] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        
        right = 1
        for j in range(n-1, -1 , -1):
            ans[j] *= right
            right *= nums[j]
        
        return ans


        