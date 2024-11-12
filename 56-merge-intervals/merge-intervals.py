class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        arr=[]
        for i in intervals:
            heapq.heappush(arr,i)
        cur=heapq.heappop(arr)
        while(arr):
            temp=heapq.heappop(arr)
            if(temp[0]>=cur[0] and temp[0]<=cur[1]):
                cur[1]=max(cur[1],temp[1])
            else:
                if cur not in ans:
                    ans.append(cur)
                cur=temp
            # print(ans,cur,temp)
        if cur not in ans:
            ans.append(cur)
        return ans