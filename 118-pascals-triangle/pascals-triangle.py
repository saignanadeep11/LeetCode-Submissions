class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,n):
            n=len(ans[-1])
            k=[1]
            for j in range(1,n):
                k.append(ans[-1][j-1]+ans[-1][j])
            k.append(1)
            ans.append(k)
        return ans