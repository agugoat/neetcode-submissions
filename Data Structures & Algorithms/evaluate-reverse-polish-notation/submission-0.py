class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        #adding stack 
        op_set = set()
        op_set.add('+')
        op_set.add('-')
        op_set.add('*')
        op_set.add('/')
        
        #going through tokens
        for i , ch in enumerate(tokens):
            # if its not a operator continue 
            if ch not in op_set:
                stack.append(int(ch))
                continue
            # do the operation 
            if ch == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif ch == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif ch == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a*b))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        
        # return the value of the stack
        return stack[-1]
            