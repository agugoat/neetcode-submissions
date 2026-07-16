class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = defaultdict(int)


        for num in nums:
            counter[num] +=1
        
        return max(counter, key=counter.get)
