# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Delete the Middle Node of a Linked List
# ║  Difficulty : Medium
# ║  Date       : 2026-06-15
# ║  URL        : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# ╚══════════════════════════════════════════════════════════════╝

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Problem Explanation:
    The goal is to delete the middle node of a singly linked list. 
    The middle node is defined as the floor(n/2)-th node (0-indexed).
    
    Approach: Two-Pointer Technique (Fast and Slow)
    1. Handle the edge case where the list has only one node. Since n=1, the middle
       node is index 0. Deleting it results in an empty list (return None).
    2. Initialize two pointers: 'slow' and 'fast'.
    3. Use a 'prev' pointer to keep track of the node immediately before 'slow'.
    4. Move 'fast' two steps and 'slow' one step at a time.
    5. When 'fast' reaches the end of the list (or the last node), 'slow' will be 
       exactly at the middle node.
    6. Delete the middle node by setting prev.next = slow.next.
    
    Time Complexity: O(N), where N is the number of nodes in the linked list. 
                     We traverse the list once.
    Space Complexity: O(1), as we only use a few pointer variables.
    """
    def deleteMiddle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        # Edge case: if the list contains only one node, the middle node is that node.
        # Deleting it leaves an empty list.
        if not head or not head.next:
            return None
        
        # 'slow' will eventually point to the middle node.
        # 'fast' moves twice as fast to find the end of the list.
        # 'prev' tracks the node before 'slow' so we can skip 'slow'.
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        # At this point, slow is the middle node and prev is the node before it.
        # Remove slow by linking prev to the node after slow.
        if prev:
            prev.next = slow.next
            
        return head
