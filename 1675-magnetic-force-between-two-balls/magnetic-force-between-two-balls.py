class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n=len(pos)
        f=pos[0]
        e=pos[n-1]
        l=0
        r=e-f
        while(l<r):
            mid=r-(r-l)//2
            nob=1
            idx=0
            start=f
            end=e
            for i in range(1,n):
                if pos[i]-start>=mid:
                    nob+=1
                    start=pos[i]
                if nob==m:
                    break
            if nob==m:
                l=mid
            else:
                r=mid-1
            # print(l,r,mid)
        return l