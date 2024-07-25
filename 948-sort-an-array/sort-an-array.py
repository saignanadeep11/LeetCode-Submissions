class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        def merge(nums,lo,mid,hi):
            # print(nums,lo,mid,hi)
            temp=[]
            p1=lo
            p2=mid+1
            while(p1<=mid and p2<=hi):
                if(nums[p1]<nums[p2]):
                    temp.append(nums[p1])
                    p1+=1
                else:
                    temp.append(nums[p2])
                    p2+=1
            while(p1<=mid):
                temp.append(nums[p1])
                p1+=1
            while(p2<=hi):
                temp.append(nums[p2])
                p2+=1
            idx=0
            for i in range(lo,hi+1):
                nums[i]=temp[idx]
                idx+=1
            return nums
        def div(nums,lo,mid,hi):
            mid=(lo+hi)>>1
            # print(lo,hi)
            if lo>=hi:
                return
            div(nums,lo,mid,mid)
            div(nums,mid+1,mid,hi)
            nums=merge(nums,lo,mid,hi)
            return nums
        nums=div(nums,0,0,len(nums)-1)
        return nums