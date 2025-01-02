class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow=['a','e','i','o','u']
        def find(i):
            if words[i][0] in vow and words[i][-1] in vow:
                return True
            return False
        n=len(words)
        words[0]=1 if find(0) else 0
        for i in range(1,n):
            words[i]=words[i-1]+1 if find(i) else words[i-1]
        m=len(queries)
        for i in range(m):
            t=queries[i]
            if t[0]==0:
                queries[i]=words[t[1]]
            else:
                queries[i]=words[t[1]]-words[t[0]-1]
        return queries