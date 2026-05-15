import numpy as np
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        output=0 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if np.abs(nums[i] - nums[j])==k: # we can do abs alone without importing numpy, but I just wanted to use it for practice
                    output +=1

        return output

                
