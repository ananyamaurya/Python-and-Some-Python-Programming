# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Number of Ways to Assign Edge Weights II
# ║  Difficulty : Hard
# ║  Date       : 2026-06-12
# ║  URL        : https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
# ╚══════════════════════════════════════════════════════════════╝

import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    """
    Problem Analysis:
    We are given a tree and queries for pairs of nodes (u, v). 
    For each pair, we need to find the number of ways to assign weights (1 or 2) 
    to the edges on the path between u and v such that the total sum of weights is odd.
    
    Mathematical Insight:
    Let 'L' be the number of edges on the path between u and v.
    Each edge can be 1 (odd) or 2 (even).
    The sum of weights is odd if and only if an odd number of edges are assigned the weight 1.
    The number of ways to choose an odd number of items from a set of L items is:
    C(L, 1) + C(L, 3) + C(L, 5) + ... = 2^(L-1)
    
    Special Case:
    If L = 0 (u == v), the path cost is 0, which is even. The number of ways is 0.
    If L > 0, the number of ways is 2^(L-1).
    
    To find L (the distance between u and v in the tree):
    L = depth[u] + depth[v] - 2 * depth[LCA(u, v)]
    where depth is the distance from the root (Node 1).
    
    Time Complexity: O(N log N + Q log N) where N is nodes and Q is queries.
    - Pre-calculating LCA takes O(N log N).
    - Each query takes O(log N) to find LCA.
    Space Complexity: O(N log N) to store the binary lifting table.
    """

    def numberOfWays(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        MOD = 10**9 + 7
        LOG = 18  # 2^17 < 10^5 < 2^18
        
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        # DFS to precompute depths and the 2^0 ancestor for binary lifting
        stack = [(1, 0, 0)] # node, parent, d
        visited = [False] * (n + 1)
        
        # Using iterative DFS to avoid recursion limit issues in some environments
        # though sys.setrecursionlimit is also provided.
        order = []
        stack = [1]
        parent = [0] * (n + 1)
        depth[1] = 0
        visited[1] = True
        
        # Build BFS/DFS order to fill 'up' table iteratively
        queue = [1]
        visited = [False] * (n + 1)
        visited[1] = True
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.append(v)
        
        # Binary Lifting Table Construction
        for i in range(1, LOG):
            for node in range(1, n + 1):
                up[node][i] = up[up[node][i-1]][i-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Lift u up to the same depth as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            
            if u == v:
                return u
            
            # Lift both u and v until their parents are the same
            for i in reversed(range(LOG)):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            
            return up[u][0]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            
            # Number of ways is 2^(dist - 1)
            results.append(pow2[dist - 1])
            
        return results
