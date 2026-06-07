# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Create Binary Tree From Descriptions
# ║  Difficulty : Medium
# ║  Date       : 2026-06-07
# ║  URL        : https://leetcode.com/problems/create-binary-tree-from-descriptions/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    The problem asks us to reconstruct a binary tree given a list of parent-child relationships.
    
    Approach:
    1. Use a hash map (dictionary) to keep track of all nodes created. This ensures 
       that we don't create duplicate TreeNode instances for the same value.
    2. Use a set to keep track of all nodes that are children. 
    3. The root of the tree is the only node that appears as a parent but never as a child.
    4. Iterate through the descriptions and link the parent to the child based on the 'isLeft' flag.
    
    Time Complexity: O(N), where N is the number of descriptions. We iterate through the 
                     descriptions list a few times.
    Space Complexity: O(N), where N is the number of nodes in the tree. We store nodes 
                      in a map and track children in a set.
    """
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Map to store value -> TreeNode mapping
        nodes = {}
        # Set to track all children to identify the root
        children = set()
        
        # First pass: create nodes and establish parent-child links
        for parent_val, child_val, is_left in descriptions:
            # Create parent node if it doesn't exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            
            # Create child node if it doesn't exist
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            
            # Establish the link
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
            
            # Mark the child node as having a parent
            children.add(child_val)
            
        # Second pass: find the root
        # The root is the node that is a parent but not a child
        for parent_val in nodes:
            if parent_val not in children:
                return nodes[parent_val]
        
        return None
