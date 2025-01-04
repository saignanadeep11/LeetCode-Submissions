class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(can)
        def find(idx,arr,k):
            if idx>=n or k>target:
                return
            if k==target:
                ans.append(arr[:])
                return
            find(idx,arr+[can[idx]],k+can[idx])
            # if arr:
            #     k-=arr.pop()
            find(idx+1,arr,k)
        find(0,[],0)
        return ans