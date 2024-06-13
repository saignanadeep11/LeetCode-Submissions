class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n=len(nums)
        self.k=self.n-k+1
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        i=bisect.bisect_left(self.nums,val)
        self.nums.insert(i,val)
        # print(self.nums)
        ans=self.nums[self.k]
        self.k+=1
        return ans

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)