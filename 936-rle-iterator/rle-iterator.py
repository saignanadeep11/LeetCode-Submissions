class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr=encoding
        self.idx=0
        self.length=len(encoding)

    def next(self, n: int) -> int:
        while(n>0):
            if(self.idx>=self.length):
                return -1
            t=self.arr[self.idx]
            if(n-t<=0):
                self.arr[self.idx]-=n
                return self.arr[self.idx+1]
            else:
                n-=t
                self.idx+=2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)