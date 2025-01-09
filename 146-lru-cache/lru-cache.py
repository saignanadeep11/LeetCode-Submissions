class LRUCache:

    def __init__(self, capacity: int):
        self.arr=[]
        self.dic=defaultdict(int)
        self.n=capacity
        self.idx=0
    def get(self, key: int) -> int:
        # print(self.arr,'get')
        if key in self.arr:
            self.arr.remove(key)
            self.arr.insert(0,key)
            # print(self.arr,key,'get')
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print(self.arr,self.idx)
        if key in self.arr:
            self.arr.remove(key)
            self.arr.insert(0,key)
            self.dic[key]=value
            return
        if self.idx>=self.n:
            k=self.arr.pop()
            if self.dic[k]:
                self.dic.pop(k)
            self.idx-=1
        self.arr.insert(0,key)
        self.dic[key]=value
        self.idx+=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)