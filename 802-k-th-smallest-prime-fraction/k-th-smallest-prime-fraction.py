class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                ans.append(str(arr[i])+'/'+str(arr[j]))
        ans.sort(key=lambda k:int(k[0:k.find('/')])/int(k[k.find('/')+1:]))

        return (int(ans[k-1][0:ans[k-1].find('/')]),int(ans[k-1][ans[k-1].find('/')+1:]))