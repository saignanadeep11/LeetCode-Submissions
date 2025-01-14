class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr=set()
        n=len(A)        
        for i in range(n):
            if A[i] in arr:
                arr.remove(A[i])
            else:
                arr.add(A[i])
            if B[i] in arr:
                arr.remove(B[i])
            else:
                arr.add(B[i])
            k=len(arr)//2
            A[i]=(i+1)-k
        return A