class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def check(i,j):
            n=len(words[i])
            m=len(words[j])
            if m<n:
                return False
            if words[i]==words[j][:n] and words[i]==words[j][m-n:]:
                return True
            return False
        ans=0
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                if check(i,j):
                    ans+=1
        return ans