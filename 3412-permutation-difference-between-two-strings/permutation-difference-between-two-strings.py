class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum=0
        for i in s:
            sum+=abs(s.find(i)-t.find(i))
        return sum