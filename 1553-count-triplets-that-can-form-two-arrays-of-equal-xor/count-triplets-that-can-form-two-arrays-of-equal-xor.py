class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pre=[0]+arr[:]
        n=len(arr)
        for i in range(n):
            pre[i+1]=pre[i]^pre[i+1]
        ans=0
        count=defaultdict(int)
        total=defaultdict(int)
        for i in range(n):
            if pre[i+1] in count:
                ans+=count[pre[i+1]]*i-total[pre[i+1]]
            count[pre[i]]+=1
            total[pre[i]]+=i
        # print(pre,count,total)
        return ans