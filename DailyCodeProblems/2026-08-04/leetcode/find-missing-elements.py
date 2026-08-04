# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Find Missing Elements
# ║  Difficulty : Easy
# ║  Date       : 2026-08-04
# ║  URL        : https://leetcode.com/problems/find-missing-elements/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

def findMissingElements(nums: List[int]) -> List[int]:
    """
    Problem Statement:
    Given an array of unique integers, the array originally contained every integer 
    between the minimum and maximum values currently present in the array.
    The task is to find and return all integers within that range that are missing 
    from the current array, sorted in ascending order.

    Approach:
    1. Identify the range: Find the minimum (start) and maximum (end) elements in the array.
    2. Track presence: Use a set for O(1) lookup time to check if a number exists in the input array.
    3. Iterate: Loop from the minimum to the maximum value. If a value is not in the set, add it to the result.

    Time Complexity: O(N + R), where N is the length of nums and R is the range (max - min).
    Space Complexity: O(N + M), where N is the size of the set and M is the number of missing elements.
    """
    
    # Step 1: Find the minimum and maximum bounds of the original range
    # Since constraints are small (nums.length <= 100), min() and max() are efficient.
    min_val = min(nums)
    max_val = max(nums)
    
    # Step 2: Convert the input list to a set for constant time lookup
    num_set = set(nums)
    
    # Step 3: Iterate through the full range and collect missing numbers
    missing_elements = []
    for i in range(min_val, max_val + 1):
        if i not in num_set:
            missing_elements.append(i)
            
    # The loop iterates in increasing order, so missing_elements is already sorted.
    return missing_elements

# Example test cases
if __name__ == "__main__":
    # Example 1
    print(f"Example 1: {findMissingElements([1, 4, 2, 5])}") # Expected: [3]
    
    # Example 2
    print(f"Example 2: {findMissingElements([7, 8, 6, 9])}") # Expected: []
    
    # Example 3
    print(f"Example 3: {findMissingElements([5, 1])}")       # Expected: [2, 3, 4]
