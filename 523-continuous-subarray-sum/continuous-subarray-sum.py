class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        pre=0
        n=len(nums)
        if n<2:
            return False
        for idx,v in enumerate(nums):
            pre+=v
            pre=pre%k
            # print(pre,d)

            # if pre==0:
            #     return True
            if pre in d:
                if idx-d[pre]>1:
                    return True
            else:
                if pre!=0:
                    d[pre]=idx
        return False