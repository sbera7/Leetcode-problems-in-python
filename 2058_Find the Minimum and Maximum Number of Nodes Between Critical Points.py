class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if head is None:
            return [-1, -1]
        current_node = head
        index = 2
        indices = []
        while current_node.next.next:
            if current_node.next.val > current_node.val and current_node.next.val > current_node.next.next.val:
                indices.append(index)

            if current_node.next.val < current_node.val and current_node.next.val < current_node.next.next.val:       
                indices.append(index)
            
            index += 1
            
            current_node = current_node.next
        
        if len(indices) < 2:
            return [-1, -1]

        else:
            min = indices[-1] - indices[0]
            for i in range(len(indices) - 1):
                if min > indices[i + 1] - indices[i]:
                    min = indices[i + 1] - indices[i]
            return [min, indices[-1] - indices[0]] 
