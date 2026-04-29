class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=1
        # for first number and index=0, we cannot compare anything. 
        # each num, we should compare it with previous num.
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
        return left 

                
           


        
       
    

        