class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0 
        j= len(nums)-1
        output=[]
        
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                output.append(nums[i]**2)
                i+=1
            else:
                output.append(nums[j]**2)
                j -=1
        return output[::-1]
