class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # for i in range(len(nums1)):
        #     if nums1[i]==0:
        #         del(nums1[i])
        # return nums1

        for j in range(len(nums2)):
            if nums2 != 0:
                nums1.append(nums2[j])
            nums1.remove(0)
        return nums1.sort()


                