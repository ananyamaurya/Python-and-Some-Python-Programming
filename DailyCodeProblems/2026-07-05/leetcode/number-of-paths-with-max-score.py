# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Number of Paths with Max Score
# ║  Difficulty : Hard
# ║  Date       : 2026-07-05
# ║  URL        : https://leetcode.com/problems/number-of-paths-with-max-score/
# ╚══════════════════════════════════════════════════════════════╝

import collections

"""
Problem Analysis:
- We need to find the maximum sum of digits from 'S' (bottom-right) to 'E' (top-left).
- Allowed moves: Up, Left, and Up-Left (Diagonal).
- Obstacles 'X' cannot be passed.
- We need to return [max_sum, number_of_paths_with_max_sum].
- Result should be modulo 10^9 + 7.

Dynamic Programming Approach:
- Let dp_sum[i][j] be the maximum sum reachable from (i, j) to the start 'S'.
- Let dp_cnt[i][j] be the number of paths that achieve that maximum sum.
- Since we move Up, Left, or Up-Left, we can process the board starting from the bottom-right
  and moving towards the top-left.

Complexity:
- Time Complexity: O(N^2), where N is the dimension of the board. We visit each cell once.
- Space Complexity: O(N^2) to store the DP tables.
"""

class Solution:
    def numberOfPathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp_sum[i][j] stores the max score to reach cell (i, j) from 'S'
        # dp_cnt[i][j] stores the number of paths achieving that max score
        dp_sum = [[-1] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]
        
        # Starting point (bottom-right)
        dp_sum[n-1][n-1] = 0
        dp_cnt[n-1][n-1] = 1
        
        # Iterate from bottom to top, right to left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip the starting cell as it's already initialized
                if r == n - 1 and c == n - 1:
                    continue
                
                # Obstacles are impassable
                if board[r][c] == 'X':
                    continue
                
                # Possible moves to reach (r, c) are from:
                # (r+1, c) -> Up
                # (r, c+1) -> Left
                # (r+1, c+1) -> Up-Left (Diagonal)
                prev_cells = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                
                max_s = -1
                count = 0
                
                for pr, pc in prev_cells:
                    if 0 <= pr < n and 0 <= pc < n:
                        # Check if the previous cell was reachable
                        if dp_sum[pr][pc] != -1:
                            if dp_sum[pr][pc] > max_s:
                                max_s = dp_sum[pr][pc]
                                count = dp_cnt[pr][pc]
                            elif dp_sum[pr][pc] == max_s:
                                count = (count + dp_cnt[pr][pc]) % MOD
                
                # If a path exists to (r, c), add current cell's value
                if max_s != -1:
                    char = board[r][c]
                    val = int(char) if char.isdigit() else 0
                    dp_sum[r][c] = max_s + val
                    dp_cnt[r][c] = count
        
        # The target is the top-left cell 'E'
        ans_sum = dp_sum[0][0]
        ans_cnt = dp_cnt[0][0]
        
        # If ans_sum is -1, it means 'E' was never reached
        if ans_sum == -1:
            return [0, 0]
        
        return [ans_sum, ans_cnt]

# Example usage:
# sol = Solution()
# print(sol.numberOfPathsWithMaxScore(["E23","2X2","12S"])) # Expected: [7, 1]
