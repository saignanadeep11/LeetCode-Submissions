class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v1,v2=0,0
        cnt1,cnt2=0,0
        for i in nums:
            if cnt1==0 and i!=v2:
                v1=i
                cnt1+=1
            elif cnt2==0 and i!=v1:
                v2=i
                cnt2+=1
            elif i==v1:
                cnt1+=1
            elif i==v2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        ans=[]
        n=len(nums)
        cnt1,cnt2=0,0
        for i in nums:
            if v1==i:
                cnt1+=1
            elif v2==i:
                cnt2+=1
        if(cnt1>n//3):
            ans.append(v1)
        if(cnt2>n//3):
            ans.append(v2)
        return ans