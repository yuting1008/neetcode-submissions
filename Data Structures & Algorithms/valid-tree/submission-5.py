class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        children = {i:[] for i in range(n)}

        for node1, node2 in edges:
            children[node1].append(node2)
            children[node2].append(node1)

        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for child in children[curr]:
                if child == prev:
                    continue
                if not dfs(child, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n