class Solution:
    def minimumPushes(self, word: str) -> int:
        d=defaultdict(int)
        for i in word:
            d[i]+=1
        ans=0
        idx=0
        push=1
        c=0
        # print(sorted(d.items()))
        for i in sorted(d.items(),key=lambda k:k[1],reverse=True):
            ans+=(push)*d[i[0]]
            idx+=1
            if idx==8:
                idx=0
                if c<=3:
                    push+=1
                c+=1
        return ans