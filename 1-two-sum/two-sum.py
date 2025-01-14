class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in dic:
                k=nums.index(target-nums[i])
                return [i,k]
            dic.add(target-nums[i])
        return []