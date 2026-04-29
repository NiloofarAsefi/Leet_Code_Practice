class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # for string, we cannot use .append()
        i=0
        j=0 
        merge_word= ""
        while i < len(word1) and j < len(word2):
            merge_word += word1[i]
            merge_word += word2[j]
            i +=1
            j +=1

        merge_word += word1[i:]
        merge_word += word2[j:]

        return merge_word
