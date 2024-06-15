class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # if k==1 and w==2 and profits==[1,2,3] and capital==[1,1,2]:
        #     return 5
        n=len(profits)
        com=[(capital[i],profits[i]) for i in range(n)]
        com.sort()
        # ans=w
        i=0
        arr=[]
        while(k>0):
            k-=1
            while i<n and com[i][0]<=w:
                heapq.heappush(arr,-com[i][1])
                i+=1
            # print(ans,w,com)
            if not arr:
                break
            w-=heapq.heappop(arr)
        return w