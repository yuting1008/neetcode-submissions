class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = {i:[] for i in range(n)}
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
        
        count = 0
        visit = set()

        def dfs(node):
            for neighbor in neighbors[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)

        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count +=1
        return count
