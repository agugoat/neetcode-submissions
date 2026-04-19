class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numSet = set(nums)
        print(numSet)

        if len(numSet) != len(nums):
            return True
            # meaning it contains a duplicate
        else:
            return False

    
         