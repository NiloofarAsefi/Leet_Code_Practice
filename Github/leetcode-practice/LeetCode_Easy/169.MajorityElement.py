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


# space O(n)
# time O(n)

# Boyer-Moore Voting Algorithm:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
    
# space O(1)
# time O(n)
