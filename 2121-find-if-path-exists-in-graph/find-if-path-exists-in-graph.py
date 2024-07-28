class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:return True
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis=set()
        st=[graph[source]]
        # print(graph,st)
        while(st):
            k=st.pop(0)
            # print(k)
            for i in k:
                if i==destination:
                    return True
                if i in vis:
                    continue
                st.append(graph[i])
                vis.add(i)
        return False