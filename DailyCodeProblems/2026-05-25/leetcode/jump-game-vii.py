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
    We need to determine if the last index of a binary string is reachable starting from index 0.
    The movement rules are: from index i, we can jump to index j if:
    1. i + minJump <= j <= i + maxJump
    2. s[j] == '0'
    
    Approach:
    A naive Dynamic Programming approach would be O(N * (maxJump - minJump)), which 
    could be O(N^2) in the worst case (e.g., minJump=1, maxJump=N).
    
    To optimize, we use a sliding window technique with a queue.
    We maintain a queue of indices that are 'reachable' and can potentially 
    serve as a starting point for a jump to the current index 'i'.
    
    As we iterate through the string:
    1. We remove indices from the front of the queue that are too far away 
       (i - index > maxJump).
    2. If the current index 'i' is '0' and there is at least one index in the 
       queue that satisfies the minJump constraint (index <= i - minJump), 
       then 'i' is reachable.
    3. If 'i' is reachable, we add it to the queue to potentially help future indices.
    
    Time Complexity: O(N) - Each index is added and removed from the queue at most once.
    Space Complexity: O(N) - In the worst case, the queue stores a significant fraction of indices.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        
        # Queue stores indices that are reachable and could potentially 
        # jump to a future index.
        reachable_indices = deque([0])
        
        # We start checking from minJump because index 0 is our start.
        for i in range(minJump, n):
            # 1. Remove indices that are beyond the maxJump range of the current index i.
            while reachable_indices and reachable_indices[0] < i - maxJump:
                reachable_indices.popleft()
            
            # 2. Check if current index i is a valid landing spot ('0').
            if s[i] == '0':
                # 3. Check if the first index in our queue satisfies the minJump requirement.
                # Since the queue is sorted, if the first element satisfies 
                # reachable_indices[0] <= i - minJump, then i is reachable.
                if reachable_indices and reachable_indices[0] <= i - minJump:
                    # If we reached the end, return True immediately.
                    if i == n - 1:
                        return True
                    # Otherwise, mark this index as reachable for future jumps.
                    reachable_indices.append(i)
        
        return False

# Example Usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Expected: True
# print(sol.canReach("01101110", 2, 3)) # Expected: False
