class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]  # flipping the sign because x + y = -a
            numMap={}   # implement a 2sum for the rest ig map was 2 slow
            left = i+1 
            right = len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right]

                if currSum == target:
                    results.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                #skip duplicats
                    while left <right and nums[left] == nums[left-1]:
                        left +=1
                
                    while left <right and nums[right] == nums[right+1]:
                        right -=1
                
                elif target > currSum:
                    left +=1
                else: 
                    right -=1
        return results
                