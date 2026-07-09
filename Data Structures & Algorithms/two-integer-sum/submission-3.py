class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = defaultdict(int)

        for i, val in enumerate(nums):
            compo = target - val

            if compo in numMap:
                return [numMap[compo],i]

            numMap[val] = i
        
        