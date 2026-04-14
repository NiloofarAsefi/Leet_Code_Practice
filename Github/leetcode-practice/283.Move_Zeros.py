class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # []
        # while not zero, add to []
        # add zero
        # return nums[:]= new_list
        #sorting at the beginning is not a good idea, it changes order of non-zero 
        list_new= []
        count_Zero =0
        for num in nums:
            if num !=0:
                list_new.append(num)
            else:
                count_Zero +=1
        while count_Zero != 0:        
            list_new.append(0)
            count_Zero -=1
        # you should change in-palce, so you should assign to nums[:] and cannot return.
        nums[:] =list_new




