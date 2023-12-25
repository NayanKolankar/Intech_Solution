class Stack:
  def __init__(self):
      self.top = -1
      self.min = float('inf')  # this will store min element
      self.a = [0] * 1000  # Maximum size of Stack




  def push(self, x):  # storing min element during push only
      if self.top >= (1000 - 1):
          return False
      else:
          self.top += 1
          self.a[self.top] = x
          if self.top == 0:
              self.min = x
              return True
          else:
              if x <= self.min:
                  self.min = x
                  return True
              else:
                  return True




  def pop(self):
      if self.top < 0:
          return -1
      else:
          x = self.a[self.top]
          self.top -= 1
          return x




  def is_empty(self):
      return self.top < 0




  def peek(self):
      if self.top < 0:
          return -1
      else:
          x = self.a[self.top]
          return x




  def min_ele(self):  # to get min element just return min
      return self.min


s = Stack()
s.push(10)
s.push(20)
s.push(5)
s.push(30)
ans = s.min_ele()
print(ans)



"""

Back and forward buttons in a web browser

The back and forward buttons on the browser can be really handy for navigating between pages. We can implement these buttons by maintaining two separate stacks. Here, we use one stack (back stack) to track links to the previously visited pages, and another stack (forward stack) to track links to the pages we have navigated away from but may want to revisit.
If we want to go back to a page we have previously visited, we can see the back button. This removes the current page from the top of the back stack and stores it on the forward stack.
If we want to move forward again, we can use the forward button, which retrieves the page from the top of the forward stack and pushes the current page onto the back stack.


"""