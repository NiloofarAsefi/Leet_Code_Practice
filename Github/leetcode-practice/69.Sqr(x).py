class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right= x
        answer =0
        while left <= right:
            mid= (left+right)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid -1
            else:
                answer = mid
                left = mid +1
        return answer
        
        # #sqr_output(x)= n
        # #n * n = x
        # # if x == 0 or x == 1:
        # #     return x
        # for numb in range(0, x+1):
        #     if numb * numb == x:
        #         return numb
        #     if numb * numb < x and (numb +1) * (numb +1) >x:
        #         return numb 

        
    




        
