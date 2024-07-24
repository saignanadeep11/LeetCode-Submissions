class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def ch(n):
            ans=0
            for i in str(n):
                # print(i,n,ans)
                ans=ans*10+mapping[int(i)]
            # print(ans)
            return int(ans)
        com=[]
        for i in nums:
            com.append([ch(i),i])
        com.sort(key=lambda x:(x[0],nums[0]))
        ret=[]
        for _,i in com:
            ret.append(i)
        return ret