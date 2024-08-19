class Solution:
    def minSteps(self, n: int) -> int:
        arr=[0]*1001
        arr[1]=0
        arr[2]=2
        arr[3]=3
        for i in range(4,n+1):
            k=i
            j=2
            while(j<=i):
                if(k%j==0):
                    k=k//j
                    arr[i]+=arr[j]
                else:
                    j+=1
            if arr[i]==0:
                arr[i]=i
        return arr[n]