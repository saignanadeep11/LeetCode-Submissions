class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        def popu(n,nums):
            count=defaultdict(int)
            for i in nums:
                count[i]+=1
            return count
        if n1>n2:
            count=popu(n2,nums2)
            nums=nums1
        else:
            count=popu(n1,nums1)
            nums=nums2
        res=[]
        for i in nums:
            if count[i]>0:
                res.append(i)
                count[i]-=1
        return res