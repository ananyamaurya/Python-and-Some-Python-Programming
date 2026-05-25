# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game VII
# ║  Difficulty : Medium
# ║  Date       : 2026-05-25
# ║  URL        : https://leetcode.com/problems/jump-game-vii/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Problem Analysis:
        We need to determine if the last index of a binary string is reachable from 
        index 0, given constraints on the jump distance [minJump, maxJump] and 
        the condition that we can only land on '0'.

        Approach:
        1. Dynamic Programming: Let dp[i] be True if index i is reachable.
        2. Transition: dp[i] is True if there exists a j such that:
           - dp[j] is True
           - s[i] == '0'
           - i - maxJump <= j <= i - minJump
        3. Optimization: Checking the range [i - maxJump, i - minJump] for any True 
           value in every step would take O(N * maxJump), which is O(N^2) in worst case.
           We can use a sliding window (prefix sum or a counter) to keep track of 
           how many reachable indices ('True' values in dp) currently exist in 
           the valid jump window.

        Time Complexity: O(N), where N is the length of the string. We traverse the string once.
        Space Complexity: O(N) to store the DP array.
        """
        n = len(s)
        if s[-1] == '1':
            return False
        
        # dp[i] indicates if index i is reachable from index 0
        dp = [False] * n
        dp[0] = True
        
        # 'reachable_count' stores the number of reachable indices (dp[j] == True)
        # within the window [i - maxJump, i - minJump].
        reachable_count = 0
        
        for i in range(1, n):
            # The window for index i is [i - maxJump, i - minJump].
            # As i increases, we need to:
            # 1. Add the new index entering the window: (i - minJump)
            # 2. Remove the index leaving the window: (i - maxJump - 1)
            
            # Add index that just entered the reach range
            if i - minJump >= 0:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # Remove index that just left the reach range
            if i - maxJump - 1 >= 0:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # If current index is '0' and there's at least one reachable index in the window
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
        
        return dp[n - 1]

# Example Walkthrough (Example 1):
# s = "011010", minJump = 2, maxJump = 3
# i=0: dp[0]=T, count=0
# i=1: window [1-3, 1-2] = [-2, -1]. count=0, s[1]='1', dp[1]=F
# i=2: window [2-3, 2-2] = [-1, 0]. dp[0] enters, count=1, s[2]='1', dp[2]=F
# i=3: window [3-3, 3-2] = [0, 1]. dp[1] enters (F), count=1, s[3]='0', dp[3]=T
# i=4: window [4-3, 4-2] = [1, 2]. dp[2] enters (F), dp[0] leaves (T), count=0, s[4]='1', dp[4]=F
# i=5: window [5-3, 5-2] = [2, 3]. dp[3] enters (T), dp[1] leaves (F), count=1, s[5]='0', dp[5]=T
# Result: dp[5] = True
