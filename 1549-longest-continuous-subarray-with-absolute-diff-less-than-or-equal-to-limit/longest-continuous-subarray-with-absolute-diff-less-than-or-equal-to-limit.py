class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans=0
        res=[]
        l=0
        nrev=[]
        # heapq.heappush(res,-10)
        # heapq.heappush(res,-18)
        # print(res)
        for i in range(len(nums)):
            heapq.heappush(res,(nums[i],i))
            heapq.heappush(nrev,(-nums[i],i))
            while res[0][1]<l:
                heapq.heappop(res)
            while nrev[0][1]<l:
                heapq.heappop(nrev)
            if -nrev[0][0]-res[0][0]<=limit:
                ans=max(ans,i-l+1)
            else:
                l+=1
                
            # print(res,nrev)
        return ans

