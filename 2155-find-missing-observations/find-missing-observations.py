class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l=len(rolls)
        rem=mean*(l+n)
        for i in rolls:
            rem-=i
        if((rem/n)>6 or rem<=0 or rem<n):
            return []
        print(l,rem,sum(rolls))
        ans=[]
        id=n
        for i in range(n):
            ans.append(rem//id)
            rem-=rem//id
            id-=1
        return ans