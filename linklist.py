class Node(object):
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList(object):
    def __init__(self): 
        self.head = Node(None)

    def InitList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def IsEmpty(self):
        p = self.head
        if p.next == None:
            print("Empty List!")
            return True 
        else:
            return False

    def Length(self):
        if self.IsEmpty():
            return False 
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def PrintList(self):
        if self.IsEmpty():
            return False
        p = self.head
        while p:
            print(p.data,end = ',')
            p = p.next
        print('')

    def GetList(self, i):
        if i > self.Length():
            print("The %d is not in the list"%i)
            return False 
        p = self.head
        index = 0
        while index < i:
            p = p.next
            index += 1
        print("data in position %d is %d" % (i, p.data))

    def Insert(self, i, data):
        if i > self.Length():
            print("Cannot insert")
            exit
        p = self.head
        index = 0
        while index < i:
            p = p.next
            index += 1

        node = Node(data)
        node.next = p.next
        p.next = node

    def Append(self,data):
        node = Node(data)
        if self.Length() == 0:
            self.head = node 
            return node
        p = self.head
        while p.next is not None:
            p = p.next 
        p.next = node
        return node 
            
        
    def Delete(self, i):
        if i > self.Length():
            print("Fail to delete")
            exit
        index = 0
        p = self.head
        while index < i:
            pre = p
            index += 1
            p = p.next
        pre.next = p.next
        p = None
        
    def Reverse(self):
        p = self.head
        q = None
        while p:
            temp = p.next
            p.next = q
            q = p
            p = temp
        self.head = q

list = LinkedList()
list.PrintList()
data = [1, 2, 1, 7, 3, 9]
list.InitList(data)
list.PrintList()
print(list.Length())
list.GetList(3)
list.Insert(3, 17)
list.PrintList()
list.Append(18)
list.PrintList()
list.Delete(4)
list.PrintList()
list.Reverse()
list.PrintList()
