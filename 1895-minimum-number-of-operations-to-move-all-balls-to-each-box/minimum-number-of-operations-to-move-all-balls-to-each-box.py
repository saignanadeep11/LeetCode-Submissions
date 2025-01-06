class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        pre=[]
        suf=[0]*n
        c=0
        for i in boxes:
            if i=='0':
                if pre:
                    pre.append(pre[-1]+c)
                else:
                    pre.append(c)
            else:
                if pre:
                    pre.append(pre[-1]+c)
                else:
                    pre.append(c)
                c+=1
        # print(pre)
        c=0
        for i in range(n-1,-1,-1):
            if boxes[i]=='0':
                if i<n-1:
                    suf[i]=suf[i+1]+c
                else:
                    suf[i]=c
            else:
                if i<n-1:
                    suf[i]=suf[i+1]+c
                else:
                    suf[i]=c
                c+=1
            pre[i]+=suf[i]
        # print(suf)
        return pre