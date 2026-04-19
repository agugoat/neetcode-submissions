class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def bt(left,right):
            if len(path) == (n * 2):
                res.append(''.join(path))
             
            if left < n:
                path.append('(')
                bt(left + 1, right)
                path.pop()
            
            if right < left:
                path.append(')')
                bt(left, right + 1)
                path.pop()
        
        bt(0,0)

        return res
            
        '''
        input: an integer
        output: list of well formed parens

        examples: n = 2
        res = [(()), ()()]

        potenital solutions:
        backtracking with constraints
        if u see ( , there must be one to account for it somewhere or keeping
        bracket counts 

        two choices

        pesduocode-
        1. start with an empty string, add either ( or ) up 

        2. if the conditon of there being more right then left break it off u feel

        3. if we reach base case of the len of string being n we should have sum 

        4. append that to a res list 
        '''