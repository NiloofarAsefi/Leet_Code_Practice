class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k



# this code has time limit exceeded.
#         max_avg=float("-inf")
        
#         for i in range(len(nums)-k+1):
#             #sum gets one iterable such as nums[i:i+k]
#             avg = sum(nums[i:i+k])/k 
#             max_avg= max(avg, max_avg)
            
#         return max_avg 
            