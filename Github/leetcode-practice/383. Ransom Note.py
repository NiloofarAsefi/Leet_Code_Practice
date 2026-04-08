class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        magazine_d = defaultdict(int)

        for ch in magazine:
            magazine_d[ch] += 1

        for ch in ransomNote:
            if magazine_d[ch] == 0:
                return False
            magazine_d[ch] -= 1
        return True 
            
#In this Q: we count the number of each ch in Magazine.

# Why defaultdict(int) works
# int gives a default value of 0, if a character is not in the dictionary yet. 
        