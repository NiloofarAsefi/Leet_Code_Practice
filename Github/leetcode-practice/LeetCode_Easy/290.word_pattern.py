class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dict_p ={}
        dict_s ={}
        s_list = s.split(' ')
        print(s_list)
        if len(pattern) != len(s_list):
            return False
    
        for a, b in zip(pattern, s_list):
            if a in dict_p and dict_p[a]!= b:
                return False
            if b in dict_s and dict_s[b] !=a:
                return False
            dict_p[a] = b
            dict_s[b] = a
        return True 
  



        