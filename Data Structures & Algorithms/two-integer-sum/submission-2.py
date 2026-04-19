class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = defaultdict(int)

        for i,num in enumerate(nums):

            compo = target - num
           
            if compo in num_map:
                return [num_map[compo], i]
            
            num_map[num] = i


    