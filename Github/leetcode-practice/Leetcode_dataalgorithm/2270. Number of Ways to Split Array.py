# define prefix
#nums= []

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix= [nums[0]]
        n= len(nums)
        for i in range(1, n):
            prefix.append(nums[i]+prefix[-1])

        ans=0
        # because the right section, should be at least one item.
        for i in range(n-1):
            sum_left= prefix[i]
            sum_right = prefix[-1]- prefix[i]
            if sum_left>= sum_right:
                ans +=1
        return ans
    
