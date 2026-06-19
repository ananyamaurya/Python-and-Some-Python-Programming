# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Find the Highest Altitude
# ║  Difficulty : Easy
# ║  Date       : 2026-06-19
# ║  URL        : https://leetcode.com/problems/find-the-highest-altitude/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Find the Highest Altitude
    Approach: Prefix Sum
    
    The problem asks for the maximum altitude reached during a trip. 
    Since we start at altitude 0, the altitude at any point 'i' is the 
    cumulative sum of all gains from the start up to that point.
    
    We maintain a running total (current_altitude) and keep track of the 
    maximum value this total reaches throughout the iteration.
    
    Time Complexity: O(n) - We iterate through the gain array exactly once.
    Space Complexity: O(1) - We only use two integer variables regardless of input size.
    """
    def largestAltitude(self, gain: list[int]) -> int:
        # The biker starts at altitude 0
        current_altitude = 0
        # Initialize max_altitude to 0 because the starting point is part of the trip
        max_altitude = 0
        
        for g in gain:
            # Update the current altitude by adding the net gain
            current_altitude += g
            
            # Update the global maximum if the current altitude is higher
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude

# Example usage and testing:
# gain = [-5, 1, 5, 0, -7] -> altitudes: [0, -5, -4, 1, 1, -6] -> max: 1
# gain = [-4, -3, -2, -1, 4, 3, 2] -> altitudes: [0, -4, -7, -9, -10, -6, -3, -1] -> max: 0
