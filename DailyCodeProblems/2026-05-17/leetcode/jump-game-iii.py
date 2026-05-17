# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game III
# ║  Difficulty : Medium
# ║  Date       : 2026-05-17
# ║  URL        : https://leetcode.com/problems/jump-game-iii/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem: Jump Game III
    The goal is to determine if we can reach an index with a value of 0, starting from a given index.
    At any index i, we can move to i + arr[i] or i - arr[i], provided the new index is within 
    the array bounds.

    Approach:
    We can use either Depth-First Search (DFS) or Breadth-First Search (BFS) to explore all 
    reachable indices. To avoid infinite loops (cycles) and redundant calculations, 
    we mark visited indices. In this implementation, we use a recursive DFS approach.
    
    Time Complexity: O(N), where N is the length of the array. In the worst case, we visit 
                     every index once.
    Space Complexity: O(N), due to the recursion stack in the worst case and the visited set.
    """

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        # A set to keep track of visited indices to prevent cycles and redundant paths
        visited = set()

        def dfs(current_index: int) -> bool:
            # Base Case 1: Out of bounds or already visited
            if current_index < 0 or current_index >= n or current_index in visited:
                return False
            
            # Base Case 2: Reached a target index with value 0
            if arr[current_index] == 0:
                return True
            
            # Mark the current index as visited
            visited.add(current_index)
            
            # Recursive step: Try jumping forward (i + arr[i]) or backward (i - arr[i])
            # If either path returns True, the goal is reachable
            return (dfs(current_index + arr[current_index]) or 
                    dfs(current_index - arr[current_index]))

        return dfs(start)

# Example usage:
# sol = Solution()
# print(sol.canReach([4,2,3,0,3,1,2], 5)) # Output: True
# print(sol.canReach([4,2,3,0,3,1,2], 0)) # Output: True
# print(sol.canReach([3,0,2,1,2], 2))     # Output: False
