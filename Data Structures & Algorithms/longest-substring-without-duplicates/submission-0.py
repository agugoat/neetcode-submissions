class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sMap = {}
        start = 0
        result = 0
        for i in range(len(s)):
            if s[i] in sMap and sMap[s[i]] >= start:
                start = sMap[s[i]] +1
            else: #calualting the result as i(index) - start+1
                result = max(result, i - start+1 )
            ## adding value to the map
            sMap[s[i]] = i
        return result

    

        


        