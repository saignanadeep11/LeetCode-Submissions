class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        def binfloor():
            lo=0
            hi=n-1
            while(lo<=hi):
                mid=(lo+hi)>>1
                if matrix[mid][0]<=target and matrix[mid][m-1]>=target:
                    return mid
                elif matrix[mid][0]>target:
                    hi=mid-1
                else:
                    lo=mid+1
            # print(lo,mid,hi)
            return mid
        row=binfloor()
        # print(row)
        def bin():
            lo=0
            hi=m-1
            while(lo<=hi):
                mid=(lo+hi)>>1
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]>target:
                    hi=mid-1
                else:
                    lo=mid+1
            return False
        return bin()