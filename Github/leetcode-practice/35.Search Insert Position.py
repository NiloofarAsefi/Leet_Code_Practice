class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left =0 
        right = len(nums)-1

# num/ 2 is a float number so we need to use // to get the integer value.

        while left <= right:
            mid = (left +right) //2
            if nums[mid]== target:
                return mid 
            elif nums[mid]< target:
                left =  mid +1
            elif nums[mid] > target:
                right = mid -1 
        return left 
# Time complexity is O(log n) because we are using binary search.
# Space complexity is O(1) because we are using constant space.      

  

        