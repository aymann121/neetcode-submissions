class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = nums1, nums2
        if len(nums1) > len(nums2): arr1, arr2 = nums2, nums1

        l,r = 0, len(arr1)-1
        half = (len(arr1) + len(arr2)) // 2
        while True:
            m = (r+l) //2
            corr = half - m - 2

            left1 = arr1[m] if m >=0 else float('-infinity')
            right1 = arr1[m+1] if m < (len(arr1) -1) else float('infinity')
            left2 = arr2[corr] if corr >= 0 else float('-infinity')
            right2 = arr2[corr+1] if corr < (len(arr2) - 1) else float('infinity')

            if left1 <= right2 and left2 <= right1:
                if (len(arr1) + len(arr2)) %2 == 1:
                    return min(right1, right2)
                return (max(left1,left2) + min(right1,right2)) / 2

            elif left1 > right2:
                r = m-1
            else:
                l = m+1

