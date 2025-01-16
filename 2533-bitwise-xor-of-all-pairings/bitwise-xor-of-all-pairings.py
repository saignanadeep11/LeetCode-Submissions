class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        if n1%2==0 and n2%2==0:
            return 0
        def find(arr,ans):
            for i in arr:
                ans=ans^i
            return ans
        if n1%2==0:
            return find(nums1,0)
        if n2%2==0:
            return find(nums2,0)
        ans=find(nums1,0)
        return find(nums2,ans)