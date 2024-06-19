class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if(n<m*k):return -1
        l=1
        r=max(bloomDay)
        while(l<r):
            mid=(l+r)//2
            nof=bo=0
            for i in bloomDay:
                if i<=mid:
                    nof+=1
                else:
                    nof=0
                if nof==k:
                    bo+=1
                    nof=0
            if bo>=m:
                r=mid
            else:
                l=mid+1
        return l