class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio=[]
        result=float('inf')
        n=len(wage)
        for i in range(n):
            ratio.append((wage[i]/quality[i],quality[i]))
        ratio.sort(key=lambda k:k[0])
        max=[]
        t=0
        for rate,q in ratio:
            heapq.heappush(max,-q)
            t+=q
            if len(max)>k:
                t+=heapq.heappop(max)
            if len(max)==k:
                result=min(result,t*rate)
        return result
