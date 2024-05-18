class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        arr=[energy[i] if i<k else 0 for i in range(n)]
        
        for i in range(k,n):
            arr[i]=max((energy[i]+arr[i-k]),energy[i])
        
        m=max(arr[-k:])
        l=max(energy[-k:])
        return max(l,m)
        