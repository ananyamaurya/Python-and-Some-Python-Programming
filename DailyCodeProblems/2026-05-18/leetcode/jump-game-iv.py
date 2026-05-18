# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game IV
# ║  Difficulty : Hard
# ║  Date       : 2026-05-18
# ║  URL        : https://leetcode.com/problems/jump-game-iv/
# ╚══════════════════════════════════════════════════════════════╝

from collections import deque, defaultdict

class Solution:
    """
    Problem Analysis:
    The goal is to find the minimum number of steps to reach the last index of an array.
    We can move to i+1, i-1, or any index j where arr[i] == arr[j].
    This is a shortest-path problem on an unweighted graph, making Breadth-First Search (BFS) 
    the ideal algorithm.

    Key Optimization:
    A naive BFS might visit all indices with the same value multiple times. 
    For example, if there are 10,000 indices with value '100', jumping from one to 
    all others repeatedly would lead to O(N^2) complexity.
    To prevent this, once we have processed all jumps for a specific value, we 
    clear the list of indices associated with that value in our map. This ensures 
    each edge (including the 'same-value' edges) is traversed at most once.

    Time Complexity: O(N)
    - Each index is added to the queue at most once.
    - Each edge (i+1, i-1, and same-value jumps) is traversed at most once due to 
      the visited set and the clearing of the value map.
    
    Space Complexity: O(N)
    - The map storing indices for each value takes O(N) space.
    - The queue and visited set take O(N) space.
    """

    def farthestJump(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Map each value to a list of indices where that value appears
        # This allows O(1) access to all possible "same-value" jump destinations
        value_map = defaultdict(list)
        for i, val in enumerate(arr):
            value_map[val].append(i)
            
        # BFS queue: (current_index, steps_taken)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            # Goal check: reached the last index
            if curr_idx == n - 1:
                return steps
            
            # Possible next moves
            next_indices = []
            
            # 1. Jump to i + 1
            if curr_idx + 1 < n:
                next_indices.append(curr_idx + 1)
            
            # 2. Jump to i - 1
            if curr_idx - 1 >= 0:
                next_indices.append(curr_idx - 1)
            
            # 3. Jump to any j where arr[curr_idx] == arr[j]
            val = arr[curr_idx]
            if val in value_map:
                for jump_idx in value_map[val]:
                    if jump_idx != curr_idx:
                        next_indices.append(jump_idx)
                
                # CRITICAL OPTIMIZATION:
                # Once we've explored all indices with the same value, 
                # we never need to explore them again from another index 
                # with the same value. This prevents O(N^2) worst-case.
                del value_map[val]
            
            for neighbor in next_indices:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
        return -1 # Should not reach here given problem constraints
