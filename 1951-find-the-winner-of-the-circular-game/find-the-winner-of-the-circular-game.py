class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        st=[i for i in range(1,n+1)]
        idx=0
        while st:
            l=len(st)
            if l<=1:
                break
            for i in range(k-1):
                m=st.pop(0)
                st.append(m)
            # print(st)
            st.pop(0)
        return st[0]

