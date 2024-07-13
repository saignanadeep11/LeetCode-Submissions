class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        com=list(zip(positions,healths,directions))
        com.sort()
        # print(com[-1][2])
        st=[]
        dic=defaultdict(int)
        # dec=0
        for pos,hea,dir in com:
            # print(st)
            l=[pos,hea,dir]
            # print(st)
            while len(st)>0 and (l and (st[-1][2]=='R' and l[2]=='L')):
                # print(st,l)
                if l and st[-1][1]>l[1]:
                    k=st.pop()
                    mk=[k[0],k[1]-1,k[2]]
                    st.append(mk)
                    l=[]
                    # print(st,"last")
                elif l and st[-1][1]<l[1]:
                    st.pop()
                    # print(l)
                    l[1]-=1
                    # st.append((pos,hea-1,dir))   
                else:
                    st.pop()
                    l=[]
            if l:
                st.append(l)
            # print(st,'end')
            # else:
            #     st.append((pos,hea,dir))
        
        for pos,hea,dir in st:
            dic[pos]=hea
        res=[]
        # print(ans)
        for i in positions:
            if dic[i]:
                res.append(dic[i])
        return res