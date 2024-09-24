class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class Trie():
            def __init__(self):
                self.root=0
                self.child={}
        def insert(root,value):
            sValue=str(value)
            n=len(sValue)
            for i in range(n):
                sVal=sValue[i]
                if sVal in root.child:
                    root=root.child[sVal]
                else:
                    nNode=Trie()
                    root.child[sVal]=nNode
                    root=root.child[sVal]
        def check(root,v):
            sValue=str(v)
            n=len(sValue)
            for i in range(n):
                sVal=sValue[i]
                if sVal in root.child:
                    root=root.child[sVal]
                else:
                    return i
            return n
        n=len(arr1)
        m=len(arr2)
        ans=0
        root=Trie()
        if n<m:
            for i in range(n):
                insert(root,arr1[i])
            for i in range(m):
                ans=max(ans,check(root,arr2[i]))
        else:
            for i in range(m):
                insert(root,arr2[i])
            for i in range(n):
                ans=max(ans,check(root,arr1[i]))
        return ans