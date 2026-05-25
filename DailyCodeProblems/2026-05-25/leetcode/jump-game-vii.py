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
    The goal is to determine if we can reach the last index of a binary string 's' 
    starting from index 0. We can jump from index i to j if:
    1. i + minJump <= j <= min(i + maxJump, s.length - 1)
    2. s[j] == '0'

    Approach:
    This is a reachability problem that can be solved using Dynamic Programming (DP).
    Let dp[i] be true if index i is reachable.
    dp[i] = (s[i] == '0') AND (there exists j such that dp[j] == true and i - maxJump <= j <= i - minJump).

    To optimize the check for the existence of a reachable 'j' in the range [i - maxJump, i - minJump],
    we can use a sliding window (specifically, a queue or a counter) to keep track of how many 
    reachable indices currently fall within the valid window.

    Time Complexity: O(N) where N is the length of the string s. We traverse the string once.
    Space Complexity: O(N) to store the dp array.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        
        # dp[i] indicates if index i is reachable from index 0
        dp = [False] * n
        dp[0] = True
        
        # reachable_count keeps track of how many indices j in the range 
        # [i - maxJump, i - minJump] have dp[j] == True.
        reachable_count = 0
        
        # We iterate through the string. For index i, the valid range of 
        # previous indices j that could jump to i is [i - maxJump, i - minJump].
        for i in range(1, n):
            # 1. Add the index that just entered the window (i - minJump)
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # 2. Remove the index that just left the window (i - maxJump - 1)
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # 3. If s[i] is '0' and there is at least one reachable index in the window,
            # then index i is reachable.
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[-1]

# Example usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Output: True
# print(sol.canReach("01101110", 2, 3)) # Output: False
