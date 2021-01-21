class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head 
        
        mid = self.findmid(head)
        
        l1 = head 
        l2 = mid.next 
        mid.next = None
        
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        
        return self.merge(l1,l2)
        
    def merge(self,l1,l2):
        dummy = ListNode(-1)
        curr = dummy 
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next 
            else:
                curr.next = l2 
                l2 = l2.next 
            curr = curr.next 
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next 
    
    
    def findmid(self,head):
        
        if not head or not head.next:
            return head
        
        slow = head 
        fast = head 
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
            
        return slow
            
