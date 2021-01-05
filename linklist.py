class Node:
    def __init__(self,val = None,next = None):
        self.val = val
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,val):
        self.length += 1
        if self.head == None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def extend(self,iterable):
        for e in iterable:
            self.append(e)

    def insert(self,idx,val):
        if idx >= self.length:
            self.append(val)
            return True
        self.length += 1
        if idx == 0:
            self.head = Node(val,self.head)
            return True
        i = 1
        p = self.head
        while i < idx:
            i += 1
            p = p.next
        p.next = Node(val,p.next)
        return True 

    def popleft(self):
        if self.head == None:
            return False
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True

    def pop(self):
        if self.head == None:
            return False
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
            return True
        p = self.head
        while p.next != self.tail:
            p = p.next
        self.tail = p
        self.tail.next = None
        return True

    def remove(self,val):
        p = self.head
        p_prev = Node(None)
        l = self.length
        while p:
            if p.val == val:
                p_prev.next = p.next
                self.length -= 1
                if p == self.head:
                    self.head = p.next
                if p == self.tail:
                    if self.head:
                        self.tail = p_prev
                    else:
                        self.tail = None 
            else:
                p_prev = p
            p = p.next
        if l == self.length:
            return False
        else:
            return True

    def clear(self):
        p = self.head
        if p == None:
            return False
        while p:
            self.head = p.next
            p = None
            p = self.head
            self.length -= 1
            
    def index(self,val):
        idx = 0
        p = self.head
        while idx < self.length:
            if p.val == val:
                print('index for %d is %d' %(val,idx))
                break
            else:
                idx += 1
                p = p.next

    def count(self,val):
        p = self.head
        count = 0
        while p:
            if p.val == val:
                count += 1
            p = p.next
        print('count of %d is %d' %(val,count))

    def reverse(self):
        p = self.head
        p_prev = None
        while p:
            next = p.next
            p.next = p_prev
            p_prev = p
            p = next
        self.head = p_prev

    def sort(self):
        if self.length > 1:
            newlist = []
            p = self.head
            while p:
                newlist.append(p.val)
                p = p.next
                newlist.sort()
            newll = LinkedList()
            newll.extend(newlist)
            newll.print_linklist()
        else:
            print(self.head.val,end ='->')
            print('None')
            print('Length: ',self.length)

    def print_linklist(self):
        p = self.head
        while p:
            print(p.val, end = '->')
            p = p.next
        print('None')
        print('Length: ',self.length)
    

List = LinkedList()
List.append(3)
List.append(4)
List.extend([4,7,1,8,5,3])
List.popleft()
List.pop()
List.insert(3,8)
List.remove(4)
List.print_linklist()
#List.clear()
List.index(5)
List.count(8)
List.reverse()
List.print_linklist()
List.sort()
