class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for ch in s: 
            if ch == '#': # if the s_Stack is not empty, pop the previous words
                if s_stack:
                    s_stack.pop()
            else: # if ch == to words, append it to stack
                s_stack.append(ch)
        for w in t:
            if  w == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(w)
        if s_stack == t_stack:
            return True 
        else:
            return False 
           
        