class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        n=len(nums2)
        for i in range(n):
            dic[nums2[i]]=i
        for i in range(len(nums1)):
            ans=-1
            for j in range(dic[nums1[i]],n):
                if nums2[j]>nums1[i]:
                    ans=nums2[j]
                    break
            nums1[i]=ans
        return nums1