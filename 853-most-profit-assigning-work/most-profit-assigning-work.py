class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans=0
        pro=list(zip(profit,difficulty))
        pro.sort(reverse=True)
        # print(pro)
        n=len(profit)
        p1=len(worker)-1
        p2=0
        worker.sort()
        while(p1>-1 and p2<n):
            # print(worker[p1],pro[p2][1],pro[p1][0],p1,p2,ans)
            if worker[p1]>=pro[p2][1]:
                ans+=pro[p2][0]
                p1-=1
            else:
                p2+=1
        return ans