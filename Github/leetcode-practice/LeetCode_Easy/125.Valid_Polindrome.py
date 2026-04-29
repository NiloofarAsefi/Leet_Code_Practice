# String 
# make all characters lowercase
#String.lower()
#make all characters uppercase 
#String.upper()

# isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers) and there is at least one character, otherwise it returns False.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s_list = []
        for ch in s:
            if ch.isalnum():
                s_list.append(ch)
            
        left =0
        right= len(s_list)-1
        while left < right:
            if s_list[left] != s_list[right]:
                return False
            left +=1
            right -=1
        return True




