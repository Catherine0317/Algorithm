class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head 
        
        o = head 
        e = o.next
        e_head = e
        
        while e and e.next:
            o.next = e.next 
            o = o.next 
            e.next = o.next 
            e = e.next 
        o.next = e_head
        return head
