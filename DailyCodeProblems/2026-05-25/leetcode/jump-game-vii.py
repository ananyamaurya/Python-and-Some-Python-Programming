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
    Problem Explanation:
    We need to determine if we can reach the last index of a binary string 's' starting 
    from index 0. We can jump from index i to index j if:
    1. j is within the range [i + minJump, i + maxJump]
    2. s[j] == '0'
    
    Approach:
    We use Dynamic Programming where dp[i] is True if index i is reachable.
    To optimize the range check [i + minJump, i + maxJump], we maintain a sliding window 
    of reachable indices. 
    
    Algorithm:
    1. Use a queue to store all indices 'j' that are reachable (dp[j] == True).
    2. For the current index 'i', we check if there's any reachable index 'prev' in the 
       queue such that:
       - prev + minJump <= i (the jump is long enough)
       - prev + maxJump >= i (the jump is not too long)
    3. If the current index 'i' is '0' and we find such a 'prev', then 'i' is reachable.
    4. We prune the queue by removing indices that are too far back to ever reach 
       any future indices (i.e., prev + maxJump < i).
    
    Time Complexity: O(N) where N is the length of the string. Each index is added 
                     and removed from the queue at most once.
    Space Complexity: O(N) to store the queue in the worst case.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        
        # Queue stores indices that are reachable and can potentially be 
        # starting points for future jumps.
        reachable_indices = deque([0])
        
        # We start iterating from index 1 to n-1
        for i in range(1, n):
            # 1. Remove indices from the front of the queue that are too far 
            # to reach the current index i.
            while reachable_indices and reachable_indices[0] + maxJump < i:
                reachable_indices.popleft()
            
            # 2. Check if the current index is '0' and if the first element in the 
            # queue can reach index i (satisfies minJump condition).
            # Since we already popped indices that exceed maxJump, we only need 
            # to check if the current index is within the reachable range of 
            # the oldest valid reachable index.
            if s[i] == '0' and reachable_indices and reachable_indices[0] + minJump <= i:
                # Index i is reachable.
                if i == n - 1:
                    return True
                reachable_indices.append(i)
        
        return False
