class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return float(self.mn_binary_search(nums1, nums2))


    def mn_binary_search(self, nums1, nums2):
        newnums = [0] * (len(nums1) + len(nums2))

        if len(newnums) == 0:
            return 0.0

        r1 = 0
        r2 = 0
        w = 0

        while w < len(newnums):
            r = 1e9

            rv1 = 1e9 if r1 >= len(nums1) else nums1[r1]
            rv2 = 1e9 if r2 >= len(nums2) else nums2[r2]

            if rv1 < rv2:
                r = rv1
                r1 += 1
            else:
                r = rv2
                r2 += 1

            newnums[w] = r
            w += 1


        if len(newnums) % 2 == 1:
            return newnums[(len(newnums))//2]
        else:
            k = len(newnums) // 2
            return (newnums[k] + newnums[k-1]) / 2.0

            