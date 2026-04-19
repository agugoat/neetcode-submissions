class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        freq = defaultdict(int)
        max_freq = 0
        ans = 0

        while right < n:
            
            freq[s[right]] +=1

            max_freq = max(freq[s[right]], max_freq)
            
            # main condtion , if broken remove the left, thus slidng the window
            while (right-left+1) - max_freq > k:
                freq[s[left]] -=1
                left+=1
            ans = max(ans, right-left + 1)

            right +=1
        
        return ans

        

        '''

        window repreents the longest seqence that meets our condtions
        the condtion to hold is , (right - left + 1 ) - max_freq > k 
        while our condtion breaks shift our left pointer up

        '''
        