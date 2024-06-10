class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        st=[]
        ans=0
        for i in s:
            n=len(st)
            if n==0:
                st.append(i)
            else:
                k=st[n-1]
                if d[k]>=d[i]:
                    ans+=d[k]
                    st.pop()
                    st.append(i)
                else:
                    ans+=d[i]-d[k]
                    st.pop()
        # print(st)
        if st:
            return ans+d[st[0]]
        return ans