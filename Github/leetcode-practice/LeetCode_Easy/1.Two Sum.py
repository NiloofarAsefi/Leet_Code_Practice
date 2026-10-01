class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solve it with hashmap
        dic= {}
        for i in range(len(nums)):
            num=nums[i]
            complement= target - num
            if complement in dic:
                return [i, dic[complement]]

            dic[num]= i

        

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return [i,j]



        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j]== target - nums[i]:
        #             return [i,j]

        # return []

# nums is not a sorted list, we cannot use pointers technique.



    
        