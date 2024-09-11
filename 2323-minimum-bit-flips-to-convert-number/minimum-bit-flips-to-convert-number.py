class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        for i in range(32):
            # print((start>>i&1),(goal>>i&1))
            if((start>>i&1)!=(goal>>i&1)):
                count+=1
        return count
        