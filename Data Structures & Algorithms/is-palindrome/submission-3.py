class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        print("this is s: "+ s)
        reversedString = s[::-1]
        print("this is rev: "+ reversedString)
        return s == reversedString
        
        