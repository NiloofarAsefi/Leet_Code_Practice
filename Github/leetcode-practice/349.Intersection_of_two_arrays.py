class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        dict_nums1= defaultdict(int)
        output =[]
        for num in nums1:
            dict_nums1[num] +=1 

        for item in nums2:
            if dict_nums1[item] !=0: 
                output.append(item)
                del dict_nums1[item]
        return output 
            


    # if dict_nums1[item] ==0:
    #     return 0
    # this is wrong because if the output should be list [] not 0. 
# space O(n)
# time O(n+m)
