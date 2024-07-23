class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        print(count)
        k=sorted(nums,key=lambda x:(count[x],-x))
        # print(k)
        return k