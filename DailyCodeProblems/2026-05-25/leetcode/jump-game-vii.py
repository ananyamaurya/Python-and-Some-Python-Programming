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
    
    Approach:
    We use Dynamic Programming to determine if the last index is reachable.
    Let dp[i] be True if index i is reachable.
    The transition is: dp[i] = True if there exists some j such that:
    - j is reachable (dp[j] == True)
    - i - maxJump <= j <= i - minJump
    - s[i] == '0'
    
    To efficiently check if any index in the range [i - maxJump, i - minJump] is reachable,
    we maintain a sliding window of reachable indices using a queue (deque).
    
    Algorithm:
    1. Initialize a queue `reachable` and add index 0 to it.
    2. Iterate through the string from index 1 to n-1.
    3. While the queue is not empty and the element at the front is too far 
       (index < i - maxJump), pop from the left.
    4. If the current index `i` is '0' and there is at least one reachable 
       index in the queue that satisfies the `minJump` constraint 
       (queue[0] <= i - minJump), then index `i` is reachable.
    5. If index `i` is reachable, add it to the queue.
    6. Return whether the last index was reachable.

    Time Complexity: O(n) - Each index is pushed and popped from the deque at most once.
    Space Complexity: O(n) - In the worst case, the deque could store O(n) indices.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # Deque stores indices 'j' that are reachable and can potentially 
        # be used to jump to a future index 'i'.
        reachable = deque([0])
        
        # We start from index 1 because index 0 is already given as reachable.
        for i in range(1, n):
            # 1. Remove indices that are out of the maxJump range for the current index i.
            while reachable and reachable[0] < i - maxJump:
                reachable.popleft()
            
            # 2. Check if the current index i can be reached from any index in the queue.
            # Condition 1: s[i] must be '0'.
            # Condition 2: There must be a reachable index j such that j <= i - minJump.
            if s[i] == '0' and reachable and reachable[0] <= i - minJump:
                # The last index is our target.
                if i == n - 1:
                    return True
                
                # Mark this index as reachable by adding it to the queue.
                reachable.append(i)
                
        # Special case: the string length might be such that the loop finishes.
        # However, the problem constraints say 2 <= s.length, and we return True 
        # inside the loop if the last index is reached.
        # If the loop finishes without returning True, it's unreachable.
        return False

# Example usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Output: True
# print(sol.canReach("01101110", 2, 3)) # Output: False
