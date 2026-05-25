# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game VII
# ║  Difficulty : Medium
# ║  Date       : 2026-05-25
# ║  URL        : https://leetcode.com/problems/jump-game-vii/
# ╚══════════════════════════════════════════════════════════════╝

import collections

class Solution:
    """
    Problem Analysis:
    We need to determine if we can reach the end of a binary string 's' starting from index 0.
    A jump from index i to j is valid if:
    1. minJump <= j - i <= maxJump
    2. s[j] == '0'
    
    Dynamic Programming Approach:
    Let dp[i] be true if index i is reachable.
    dp[i] is true if there exists some j such that:
    i - maxJump <= j <= i - minJump AND dp[j] is true AND s[i] == '0'.
    
    Optimization:
    Checking all j in the range [i - maxJump, i - minJump] would take O(N * (maxJump - minJump)), 
    which is O(N^2) in worst case. We can optimize this using a sliding window sum 
    or a queue to keep track of reachable indices in the current valid jump window.
    
    Time Complexity: O(N) - Each index is added and removed from the queue at most once.
    Space Complexity: O(N) - To store the reachability state or the queue.
    """
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        
        # reachable_indices stores indices 'j' that are marked as reachable
        # and are within the window that can potentially jump to the current index 'i'.
        reachable_indices = collections.deque()
        
        # Starting position is always reachable
        reachable_indices.append(0)
        
        # We start checking from index 1.
        # For index i to be reachable, there must be a reachable index j in [i - maxJump, i - minJump].
        for i in range(1, n):
            # 1. Remove indices from the queue that are too far back to reach index i
            while reachable_indices and reachable_indices[0] < i - maxJump:
                reachable_indices.popleft()
            
            # 2. Check if the current index i can be reached from any index in the queue.
            # The index must be at least minJump distance away.
            if s[i] == '0' and reachable_indices and reachable_indices[0] <= i - minJump:
                # Index i is reachable!
                if i == n - 1:
                    return True
                reachable_indices.append(i)
                
        return False

# Example Usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3))  # Output: True
# print(sol.canReach("01101110", 2, 3)) # Output: False
