class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        class Tri:
            def __init__(self,root):
                self.root=root
                self.children={}
           
        def insert(root,value):
            sValue=str(value)
            n=len(sValue)
            for i in range(n):
                val=int(sValue[:i+1])
                if val in root.children:
                    root=root.children[val]
                else:
                    nNode=Tri(0)
                    root.children[value]=nNode
        TrieRoot=Tri(0)
        for i in range(1,n+1):
            insert(TrieRoot,i)
        ans=[]
        def dfs(TrieRoot):
            arr=TrieRoot.children
            for i in arr:
                ans.append(i)
                dfs(TrieRoot.children[i])
        dfs(TrieRoot)
        return ans