class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {")": "(", "]":"[", "}": "{"}
        for ch in s:
            if ch in ")]}":
                if stack and stack[-1] == mapped[ch]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(ch)
                
        return stack ==[]
            
        