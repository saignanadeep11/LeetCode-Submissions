class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        for i in nums:
            heapq.heappush(arr,i)
            if len(arr)>k:
                heapq.heappop(arr)
        return heapq.heappop(arr)