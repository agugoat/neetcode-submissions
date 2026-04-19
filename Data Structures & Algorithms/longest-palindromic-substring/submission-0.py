class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ''
        longest = 0
        start = 0
        end = 0
        n = len(s)

        for i in range(n):
            
            # odd case
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:

                if (right - left + 1 ) > longest:
                    longest = right - left + 1
                    end = right
                    start = left

                right +=1
                left -= 1
            
            #even case
            left = i
            right = i+1

            while left >= 0 and right < n and s[left] == s[right]:

                if (right - left + 1 ) > longest:
                    longest = right - left + 1
                    end = right
                    start = left

                right +=1
                left -= 1
        return s[start:end +1]

