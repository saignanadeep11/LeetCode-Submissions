class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.n=len(nums)
        nums.sort()
        self.nums=nums

    def add(self, val: int) -> int:
        idx=bisect.bisect_right(self.nums,val)
        self.nums.insert(idx,val)
        self.n+=1
        return self.nums[self.n-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)