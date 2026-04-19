class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = defaultdict(int)
        need = defaultdict(int)
        min_len = float('inf')
        n = len(s)
        
        for c in t:
            need[c] +=1
        print(need)
        required = len(need)
        formed = 0
        left = 0

        for i in range(n):
            window[s[i]] +=1 

            if s[i] in need and window[s[i]] == need[s[i]]:
                formed +=1
            # shrink
            while formed == required:
                if (i - left + 1) < min_len:
                    min_len = (i - left + 1)
                    res_start = left
                    res_end = i
                
                char_to_remove = s[left]
                window[char_to_remove] -=1

                if char_to_remove in need and window[char_to_remove] < need[char_to_remove]:
                    formed-=1
                s
                left +=1

        
        return "" if min_len == float('inf') else s[res_start:res_end+1]
                








        