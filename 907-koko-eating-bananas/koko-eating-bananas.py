class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        
        lo=1
        hi=max(piles)
        def find(x):
            hours=h
            b=0
            idx=0
            while(hours>=0):
                if idx>=n:
                    return True
                if idx<n:
                    b=piles[idx]
                    idx+=1
                cost=int(math.ceil(b/x))
                # print(math.ceil(b/x))
                hours-=cost
                # print(b,x)
            return b==0 and idx==n
        while(lo<=hi):
            mid=(lo+hi)>>1
            if(find(mid)):
                hi=mid-1
            else:
                lo=mid+1
            # print(lo,mid,hi)
        return lo