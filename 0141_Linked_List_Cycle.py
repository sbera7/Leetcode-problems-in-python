# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        hash_set = []
        if head is None:
            return False
        while head.next:
            if head.next in hash_set:
                return True
            hash_set.append(head.next)
            head = head.next
        
        return False
