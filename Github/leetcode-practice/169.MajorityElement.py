class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        n = len(nums)
        output_d = defaultdict(int)
        for num in nums: 
            output_d[num] += 1 
        
        for num in nums: 
            if output_d[num] > n/2:
                return num 


