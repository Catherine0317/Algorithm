class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head 
        
        curr = head 
        next = curr.next 
        
        while curr and next:
            if curr.val == next.val:
                curr.next = next.next
            else:
                curr = next
            next = next.next
        return head 
