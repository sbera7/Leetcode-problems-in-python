class Solution(object):
    def mergeNodes(self, head):
        current_node = head
        sum = 0
        res = []
        
        while current_node.next:
            current_node = current_node.next
            sum = sum + current_node.val

            if current_node.val == 0:
                res.append(sum)
                sum = 0
        
        
        for i, n in enumerate(res):
            if i == 0:
                up_res = ListNode(n)
                current_node = up_res
            
            else:
                current_node.next = ListNode(n)
                current_node = current_node.next
            
        return up_res
