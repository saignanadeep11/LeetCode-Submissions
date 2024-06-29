class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
       
        for i in range(len(edges)):
            edges[i][0], edges[i][1] = edges[i][1], edges[i][0]
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1]) 
        cache = {}
        def dfs(node):
            if node in cache: return cache[node]
            children = set([node])
            for next_node in graph[node]:
                children |= dfs(next_node) 
            cache[node] = children
            return cache[node]
        res = []
        for i in range(n):
            res_i = dfs(i).copy()
            res_i.remove(i) 
            res.append(sorted(list(res_i))) 
        return res
            