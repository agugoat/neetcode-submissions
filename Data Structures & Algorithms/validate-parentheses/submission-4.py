class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackMap = {')':'(', ']':'[', '}':'{'}

        for char in s:
           #if it is opening bar
            if char in brackMap.values():
               stack.append(char)
            elif char in brackMap:
                if stack and stack[-1] == brackMap[char]:
                    stack.pop()
                else:
                    return False
            
        return 0 == len(stack)

                    
              
        
        