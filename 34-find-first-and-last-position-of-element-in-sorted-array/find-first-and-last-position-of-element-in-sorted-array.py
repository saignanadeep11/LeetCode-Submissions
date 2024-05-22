class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def floor(arr,k):
            p1=0
            p2=len(arr)-1
            mid=0
            while p1<=p2:
                mid=(p1+p2)>>1
                if arr[mid]==k:
                    p2=mid-1
                elif(arr[mid]>k):
                    p2=mid-1
                else:
                    p1=mid+1
            return(p1)
        def ceil(arr,k):
            p1=0
            p2=len(arr)-1
            mid=0
            while p1<=p2:
                mid=(p1+p2)>>1
                if arr[mid]==k:
                    p1=mid+1
                elif(arr[mid]>k):
                    p2=mid-1
                else:
                    p1=mid+1
            return(p2)
        sm=floor(nums,target)
        la=ceil(nums,target)
        if(sm>la):
            return [-1,-1]
        return [sm,la]
        