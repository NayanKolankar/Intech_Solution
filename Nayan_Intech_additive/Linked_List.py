class Node:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next




class LinkedList:
   def __init__(self):
       self.head = None


   def insert(self, val):
       newNode = Node(val)
       newNode.next = self.head
       self.head = newNode
       return self.head




def nfromend(head, n):
   fast = head
   slow = head
   for i in range(n):
       fast = fast.next
   if fast == None:
       return -1
   while fast.next != None:
       fast = fast.next
       slow = slow.next
   ans = slow.val
   return ans




l = LinkedList()
head = Node()


head = l.insert(10)
head = l.insert(5)
head = l.insert(40)
head = l.insert(3)
head = l.insert(3)


k = int(input("enter the index to find number from last\n"))
ans = nfromend(head, k)
print(ans)