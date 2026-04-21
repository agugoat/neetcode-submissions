class Solution:
            def subarraySum(self, nums: List[int], k: int) -> int:
                        n = len(nums)
                        count_map = defaultdict(int)
                        count_map[0] = 1
                        running_sum = 0
                        ans = 0

                        for i in range(n):
                            running_sum += nums[i]
                            ans += count_map[running_sum-k]
                            count_map[running_sum] +=1
                        return ans

                       
