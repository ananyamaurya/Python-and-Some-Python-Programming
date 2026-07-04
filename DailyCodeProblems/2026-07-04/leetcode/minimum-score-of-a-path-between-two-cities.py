# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Minimum Score of a Path Between Two Cities
# ║  Difficulty : Medium
# ║  Date       : 2026-07-04
# ║  URL        : https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# ╚══════════════════════════════════════════════════════════════╝

"""
Problem Analysis:
The problem asks for the "minimum score" of a path between city 1 and city n. 
The score of a path is defined as the minimum edge weight along that path.
Crucially, the problem allows us to traverse any road multiple times. This means if we can 
reach any node in a connected component, we can include any edge within that connected 
component in our path by simply traveling to that edge and coming back.

Therefore, the "minimum score" is simply the minimum weight of any edge 
belonging to the connected component that contains both city 1 and city n.

Algorithm:
1. Use a graph traversal (BFS or DFS) or Union-Find to identify all nodes and 
   edges in the connected component containing city 1.
2. While traversing, keep track of the minimum edge weight encountered.
3. Since the problem guarantees a path exists between 1 and n, they will be in 
   the same component.

Complexity:
- Time Complexity: O(V + E), where V is the number of cities (n) and E is 
  the number of roads. We visit each node and edge once.
- Space Complexity: O(V + E) to store the adjacency list and the visited set.
"""

from collections import deque

class Solution:
    def minimumScore(self, n: int, roads: list[list[int]]) -> int:
        # Create an adjacency list for the graph
        # adj[u] = [(neighbor, weight), ...]
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Use BFS to find all edges in the component containing city 1
        # We want to find the minimum edge weight in this component
        min_score = float('inf')
        visited = {1}
        queue = deque([1])
        
        while queue:
            u = queue.popleft()
            
            for v, weight in adj[u]:
                # Update the global minimum edge weight found in this component
                min_score = min(min_score, weight)
                
                # If the neighbor hasn't been visited, add it to the queue
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
                    
        return min_score

# Example usage:
# sol = Solution()
# print(sol.minimumScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])) # Output: 5
# print(sol.minimumScore(4, [[1,2,2],[1,3,4],[3,4,7]]))         # Output: 2
