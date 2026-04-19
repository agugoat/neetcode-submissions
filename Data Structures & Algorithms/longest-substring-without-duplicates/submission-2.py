class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0
        right = 0
        seen = set()
        res = 0

        while right < n:

            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            right +=1

            res = max(res, right - left)

        return res


        