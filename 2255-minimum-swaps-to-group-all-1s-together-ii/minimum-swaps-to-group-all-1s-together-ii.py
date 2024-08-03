class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def side(val):
            count=nums.count(val)
            ma=-1
            ans=0
            for i in range(count):
                if nums[i]==val:
                    ans+=1
                ma=max(ma,ans)
            p2=count
            p1=0
            while(p2<len(nums)):
                if nums[p1]==val:
                    ans-=1
                if nums[p2]==val:
                    ans+=1
                ma=max(ma,ans)
                p1+=1
                p2+=1
            # print(ma)
            return count-ma
        return min(side(0),side(1))