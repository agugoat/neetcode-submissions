class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        print(s)
        t = ''.join(sorted(t))

        return t == s

        
        