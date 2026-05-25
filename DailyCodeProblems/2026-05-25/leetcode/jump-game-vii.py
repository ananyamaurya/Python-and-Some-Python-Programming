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
    Problem: Jump Game VII
    The goal is to determine if we can reach the last index of a binary string 's'
    starting from index 0, given the jumping constraints [minJump, maxJump] 
     and the requirement that the destination index must contain '0'.

    Approach:
    We use Dynamic Programming where dp[i] is True if index i is reachable.
    To avoid an O(N * maxJump) complexity, which would be O(N^2) in worst case,
    we use a sliding window approach.
    
    We maintain a count of reachable indices ('0's that are reachable) within the 
    current window [i - maxJump, i - minJump]. 
    If the current index i is '0' and there is at least one reachable index in the 
    window, then index i becomes reachable.

    Time Complexity: O(N) - We traverse the string once.
    Space Complexity: O(N) - To store the reachability status of each index.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # dp[i] indicates if index i is reachable from index 0
        dp = [False] * n
        dp[0] = True
        
        # 'reachable_count' tracks how many indices in the current window [left, right]
        # are both '0' and reachable.
        reachable_count = 0
        
        # The window for index i is [i - maxJump, i - minJump].
        # We maintain this window as we iterate i from 1 to n-1.
        for i in range(1, n):
            # The right edge of the window for the current index i is (i - minJump)
            # If this index is within bounds and is reachable, add it to our count.
            right = i - minJump
            if right >= 0:
                if dp[right]:
                    reachable_count += 1
            
            # The left edge of the window is (i - maxJump - 1)
            # As i increases, the index that just fell out of the window is (i - maxJump - 1)
            left = i - maxJump - 1
            if left >= 0:
                if dp[left]:
                    reachable_count -= 1
            
            # If current character is '0' and there is at least one reachable 
            # index in the current window, mark current index as reachable.
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
        
        return dp[n - 1]

# Example Usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Expected: True
# print(sol.canReach("01101110", 2, 3)) # Expected: False
