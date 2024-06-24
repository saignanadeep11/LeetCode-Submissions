class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans=0
        ischeck=0
        n=len(nums)
        flag=[0]*n
        for i in range(n):
            ischeck+=flag[i]
            num=nums[i]^1 if ischeck%2 else nums[i]
            nums[i]=num

            if num==0:
                if i+k>n:
                    return -1
                nums[i]^=1
                if i+k<n:
                    flag[i+k]=-1
                ischeck+=1
                ans+=1
        return ans