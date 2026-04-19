class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sOrder = ''.join(sorted(s))
        print(sOrder)
        tOrder = ''.join(sorted(t))
        print(tOrder)

        return sOrder == tOrder