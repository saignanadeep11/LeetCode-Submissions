class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n=len(arr)
        arr1=defaultdict(int)  
        arr2=defaultdict(int)
        for i in range(n):
            arr1[target[i]]+=1
            arr2[arr[i]]+=1
        if arr1!=arr2:
            return False
        return True