class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        merged = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        # If either list1 or list2 is not empty, append it to the merged list
        if list1 is not None:
            merged.next = list1
        if list2 is not None:
            merged.next = list2
        
        return dummy.next
