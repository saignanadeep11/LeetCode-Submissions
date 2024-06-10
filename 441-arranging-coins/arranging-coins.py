class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(n):
            t=((i*(i-1))//2)+i
            # print(t)
            if t==n:
                return i
            if t>n:
                return i-1
        return 1