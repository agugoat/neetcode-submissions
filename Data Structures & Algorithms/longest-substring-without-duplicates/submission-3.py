class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        right = 0
        n = len(s)
        max_len = 0

        while right < n:

            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            else:
                seen.add(s[right])
        
            max_len = max(max_len, len(seen))            
            right+=1
        
        return max_len
        