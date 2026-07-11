# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Count the Number of Complete Components
# ║  Difficulty : Medium
# ║  Date       : 2026-07-11
# ║  URL        : https://leetcode.com/problems/count-the-number-of-complete-components/
# ╚══════════════════════════════════════════════════════════════╝

from collections import deque

class Solution:
    """
    Problem: Count the Number of Complete Components
    
    Approach:
    1. Represent the graph using an adjacency list.
    2. Use Breadth-First Search (BFS) or Depth-First Search (DFS) to identify all connected components.
    3. For each connected component:
       - Count the number of nodes (V) in that component.
       - Count the number of edges (E) within that component.
    4. A connected component is "complete" (a clique) if every node is connected to every other node.
       In a complete graph with V vertices, the total number of edges is V * (V - 1) / 2.
    5. Count how many components satisfy this condition.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
                     We visit each node and edge once during the BFS traversal.
    Space Complexity: O(V + E) to store the adjacency list and the visited array.
    """

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        for i in range(n):
            if not visited[i]:
                # Found a new connected component
                component_nodes = []
                queue = deque([i])
                visited[i] = True
                
                # Standard BFS to find all nodes in the component
                while queue:
                    u = queue.popleft()
                    component_nodes.append(u)
                    for neighbor in adj[u]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # To verify if the component is complete:
                # Let V be the number of nodes in the component.
                # Each node in a complete component must have a degree exactly equal to V - 1.
                v_count = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    # If any node in the component doesn't connect to all other nodes in the same component
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count

# Example Usage:
# sol = Solution()
# print(sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]])) # Output: 3
# print(sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]])) # Output: 1
