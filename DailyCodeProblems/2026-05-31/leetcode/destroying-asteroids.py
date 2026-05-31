# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Destroying Asteroids
# ║  Difficulty : Medium
# ║  Date       : 2026-05-31
# ║  URL        : https://leetcode.com/problems/destroying-asteroids/
# ╚══════════════════════════════════════════════════════════════╝

import collections

class Solution:
    """
    Problem: Destroying Asteroids
    
    The goal is to determine if a planet of a given mass can destroy all asteroids in a provided list.
    A planet can destroy an asteroid if its current mass is greater than or equal to the asteroid's mass.
    Upon destruction, the planet absorbs the asteroid's mass.
    
    Greedy Strategy:
    To maximize the chances of destroying all asteroids, the planet should always target the 
    smallest available asteroid first. By destroying smaller asteroids, the planet increases 
    its mass as much as possible before attempting to destroy larger asteroids.
    
    Approach:
    1. Sort the asteroids in non-decreasing order.
    2. Iterate through the sorted list.
    3. If the planet's current mass is >= the current asteroid's mass, add the asteroid's mass 
       to the planet.
    4. If the planet's mass is < the asteroid's mass at any point, it's impossible to proceed 
       further, so return False.
    5. If all asteroids are processed, return True.
    
    Time Complexity: O(N log N) where N is the number of asteroids. 
                     The complexity is dominated by the sorting step.
    Space Complexity: O(1) or O(N) depending on the sorting implementation's auxiliary space.
    """
    
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort asteroids in ascending order to follow the greedy approach
        asteroids.sort()
        
        current_mass = mass
        
        for asteroid_mass in asteroids:
            # Check if the planet can destroy the current smallest asteroid
            if current_mass >= asteroid_mass:
                # Absorb the mass of the destroyed asteroid
                current_mass += asteroid_mass
            else:
                # If the planet cannot destroy the smallest available asteroid, 
                # it cannot destroy any remaining asteroids.
                return False
        
        # All asteroids were successfully destroyed
        return True

# Example usage:
# sol = Solution()
# print(sol.asteroidsDestroyed(10, [3,9,19,5,21])) # Output: True
# print(sol.asteroidsDestroyed(5, [4,9,23,4]))   # Output: False
