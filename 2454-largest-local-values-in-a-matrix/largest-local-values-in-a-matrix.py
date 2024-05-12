class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(grid)
        m=n-2
        ''' 
        ij
        i=2 times
        j=2 times
        00,01,02
        10,11,12
        20,21,22

        01,02,03
        11,12,13
        21,22,23

        10,11,12
        20,21,22
        30,31,33

        11,12,13
        21,22,23
        31,32,33        
        '''
        def find(i,j):
            arr=[]
            for ri in range(3):
                for cj in range(3):
                    arr.append(grid[i+ri][j+cj])
            return max(arr)
        for i in range(n-2):
            arr=[]
            for j in range(n-2):
                arr.append(find(i,j))
            ans.append(arr)
        return ans
