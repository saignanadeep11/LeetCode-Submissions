class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def rem(s,f,n,x):
            ans=0
            st=[]
            for i in s:
                if st and st[-1]==f and i==n:
                    ans+=x
                    st.pop()
                else:
                    st.append(i)
            return ''.join(st),ans
        if x>y:
            s,ans1=rem(s,'a','b',x)
            s,ans=rem(s,'b','a',y)
        else:
            s,ans=rem(s,'b','a',y)
            s,ans1=rem(s,'a','b',x)
        return ans+ans1