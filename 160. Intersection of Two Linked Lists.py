# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
        
        a = headA
        b = headB
        c = p1
        
        if p1 == None:
            a = headB
            b = headA
            c = p2
        
        while c != None:
            a = a.next
            c = c.next
        
        while a != b:
            a = a.next
            b = b.next
        
        return a
