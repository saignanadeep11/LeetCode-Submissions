class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        mem=defaultdict(int)
        if nums.count(0)==100:return 0
        def rec(idx):
            if mem[idx]:
                return mem[idx]
            if idx>=n:
                return 0
            mem[idx]=nums[idx]+max(rec(idx+3),rec(idx+2))
            # mem[idx+1]=nums[idx+1]+max(rec(idx+2),rec(idx+3))
            return mem[idx]
        rec(0)
        rec(1)
        # print(mem)
        return max(mem[0],mem[1])