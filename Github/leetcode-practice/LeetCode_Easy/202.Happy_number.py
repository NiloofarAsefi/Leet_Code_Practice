class Solution:
    def isHappy(self, n: int) -> bool:
        # turn number to str: str(n)
        # turn ch in str to int: int(ch)
        # ^ means bitwise XOR, not power.
        # square: ** 2  
# List
#ordered
#can have duplicates
#use .append()
#Set
#unique values only
#no duplicates
#use .add()
        seen = set()
        while n !=1: 
            total = 0
            num_str=str(n)    
            for ch in num_str:
                total += int(ch)**2
            if total in seen:
                return False  
            seen.add(total)
            n = total
        return True


        

