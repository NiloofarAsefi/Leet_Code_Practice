class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n= len(haystack)
        m= len(needle)

        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i   
             
        return -1
    
# A sliding window means:
#you look at a continuous part of the string or array
#that part is called the window
#then you move that window step by step

#first window: haystack[0:m]
#next window: haystack[1:1+m]
#next window: haystack[2:2+m]