# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Left and Right Sum Differences
# ║  Difficulty : Easy
# ║  Date       : 2026-06-06
# ║  URL        : https://leetcode.com/problems/left-and-right-sum-differences/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem Analysis:
    The goal is to compute an array where each element at index i is the absolute 
    difference between the sum of all elements to the left of i and the sum of 
    all elements to the right of i.

    Approach:
    1. Calculate the total sum of the input array `nums`.
    2. Use a running variable `left_sum` (initialized to 0) to keep track of the 
       sum of elements encountered so far as we iterate through the array.
    3. For any index `i`, the `right_sum` can be derived as:
       right_sum = total_sum - left_sum - nums[i].
    4. The result for index `i` is then |left_sum - right_sum|.
    5. Update `left_sum` by adding the current element `nums[i]` before moving 
       to the next index.

    Time Complexity: O(n) where n is the length of the array. We traverse the array twice 
                     (once for total sum, once to build the answer).
    Space Complexity: O(n) to store the result array.
    """

    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Calculate the total sum of the array to derive rightSum efficiently
        total_sum = sum(nums)
        n = len(nums)
        
        # Initialize the answer array
        answer = [0] * n
        
        # Running sum of elements to the left of the current index
        left_sum = 0
        
        for i in range(n):
            # Calculate sum of elements to the right of index i
            # Total = left_sum + current_element + right_sum
            right_sum = total_sum - left_sum - nums[i]
            
            # Store the absolute difference
            answer[i] = abs(left_sum - right_sum)
            
            # Update left_sum for the next index
            left_sum += nums[i]
            
        return answer

# Example Usage:
# sol = Solution()
# print(sol.leftRightDifference([10, 4, 8, 3]))  # Output: [15, 1, 11, 22]
# print(sol.leftRightDifference([1]))            # Output: [0]
