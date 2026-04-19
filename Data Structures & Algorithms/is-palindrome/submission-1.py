class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s is None:
            return false
       
        s = ''.join(char.lower() for char in s if char.isalnum())

       
        # left being the starting index at 0
        left = 0
        # right being the full length of the string 
        right = len(s)-1

        while (left < right):
            if(s[left] != s[right]):
                return False
            left+=1
            right-=1
        return True
        
        