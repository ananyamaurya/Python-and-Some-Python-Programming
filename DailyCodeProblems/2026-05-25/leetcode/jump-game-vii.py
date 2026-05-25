# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game VII
# ║  Difficulty : Medium
# ║  Date       : 2026-05-25
# ║  URL        : https://leetcode.com/problems/jump-game-vii/
# ╚══════════════════════════════════════════════════════════════╝

from collections import deque

class Solution:
    """
    Problem Analysis:
    We need to determine if we can reach the last index of a binary string 's',
    starting from index 0. We can jump from index i to index j if:
    1. minJump <= j - i <= maxJump
    2. s[j] == '0'

    Dynamic Programming Approach:
    Let dp[i] be true if index i is reachable.
    dp[i] = s[i] == '0' AND there exists some k such that:
            i - maxJump <= k <= i - minJump AND dp[k] == true.

    Optimization:
    Checking all k in the range [i - maxJump, i - minJump] for every i would lead to 
    O(N * (maxJump - minJump)) complexity, which is O(N^2) in the worst case.
    We can use a sliding window (specifically a deque or a counter) to maintain the 
    number of reachable indices (where dp[k] == true) within the current valid window.

    Time Complexity: O(N) - We traverse the string once.
    Space Complexity: O(N) - To store the dp array.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # dp[i] indicates if the index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # reachable_count tracks how many indices in the current window [i - maxJump, i - minJump]
        # are marked as True in the dp array.
        reachable_count = 0
        
        # We start checking reachability from index minJump because 
        # any index before that cannot be reached from index 0.
        for i in range(1, n):
            # 1. Add the new index that just entered the window [i - maxJump, i - minJump]
            # The index entering the window for current 'i' is (i - minJump)
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # 2. Remove the index that just left the window
            # The index leaving the window for current 'i' is (i - maxJump - 1)
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # 3. Determine if index i is reachable
            # It is reachable if s[i] is '0' and there's at least one reachable index in the window
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
        
        return dp[n - 1]

# Example usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3))   # Expected: True
# print(sol.canReach("01101110", 2, 3)) # Expected: False
