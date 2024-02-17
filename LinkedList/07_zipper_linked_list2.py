
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z


def zipper_lists_2(head1, head2):
    current1 = head1
    current2 = head2

    while current1.next and current2: # while list 1 have not finished

        # Catch the next values before overwrite
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        # update currents 
        current1 = next1
        current2 = next2

    
    if current2: # if list 2 is longer than list 1
        current1.next = current2

    return head1



def zipper_lists_3(head_1, head_2):
  current = head_1

  current_1 = head_1.next
  current_2 = head_2
  
  count = 0

  while current_1 and current_2: # both are not None

    if count % 2 == 0:
      current.next = current_2
      current_2 = current_2.next
    else:
      current.next = current_1
      current_1 = current_1.next

    current = current.next
    count += 1
    
  if current_1: # if current_1 is not None
    current.next = current_1
  if current_2: # if current_2 is not None
    current.next = current_2
    
  return head_1
 



if __name__ == "__main__":
   def linked_list_values(current):
    values = []
    while current != None: 
        values.append(current.value)
        current = current.next
        #print(current)

    return values

   #print(reverse_list_2(a)) # 'c'
   #print(linked_list_values(reverse_list(a)))
   print(linked_list_values(zipper_lists_2(x, a)))

