class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # res=sys.maxsize
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            idx=0
            ma=-1
            mi=min(matrix[i])
            idx=matrix[i].index(mi)
            for j in range(m):
                # print(j,idx)
                ma=max(matrix[j][idx],ma)
                # idx+=1
            # print(mi,ma)
            if ma==mi:
                ans.append(ma)
        return ans