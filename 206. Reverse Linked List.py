class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr = head 
        prev = None 
        next = None 
        
        while curr != None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next 
        return prev
