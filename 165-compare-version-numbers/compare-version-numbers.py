class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        n1=len(s1)
        n2=len(s2)
        p1=p2=0
        t1=t2=''
        def check(t1,t2):
            t1=int(t1)
            t2=int(t2)
            # print(t1,t2)
            if(t1>t2):
                return 1
            elif t1<t2:
                return -1
            return 0
        while(p1<n1 and p2<n2):
            while p1!=n1 and s1[p1]!='.':
                t1+=s1[p1]
                p1+=1
            while p2!=n2 and (s2[p2]!='.'):
                t2+=s2[p2]
                p2+=1
            if p1==n1 or p2==n2 or(s1[p1]=='.' and s2[p2]=='.'):
                k=check(t1,t2)
                t1=t2=''
                if(k!=0):
                    return k
                p1+=1
                p2+=1
            # print(s1[p1-1],s2[p2-1])
            # print(t1,t2)
        # print(p1,/p2)
        while(p1<n1):
            # print(s1[p1])
            while p1!=n1 and s1[p1]!='.':
                t1+=s1[p1]
                p1+=1
            if p1==n1 or(s1[p1]=='.'):
                t1=int(t1)
                
                if(t1>0):
                    return 1
                
                p1+=1
                t1=''

        while(p2<n2):
            while p2!=n2 and (s2[p2]!='.'):
                t2+=s2[p2]
                p2+=1
            if p2==n2 or(s2[p2]=='.'):
                t2=int(t2)
                if(t2>0):
                    return -1
                
                t2=''
                p2+=1
        return 0