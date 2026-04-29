     
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s= {}
        dict_t= {}

        for a, b in zip(s, t):
            # checking if the key is in the dictionary.
            if a in dict_s and dict_s[a] !=b:
                return False 

            if b in dict_t and dict_t[b] != a:
                return False 
            
            # making the dictionry for both string, if the key is not in the dictionary, it will add the key and value to the dictionary
            dict_s[a]=b
            dict_t[b]=a
        return True 

        
# zip() is a Python function that lets you loop through two things at the same time.
# With defaultdict(int), the default value is 0, which is useful for counting,
# here we not counting in dictionary, so we can define {}



        