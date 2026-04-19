class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        print(numSet)
        return len(numSet) != len(nums)
         