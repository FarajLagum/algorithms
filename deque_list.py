# A linear data structure in which elements may be appended to or popd from either end.
# # Deque implementaion in python with lists

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def append_rear(self, item):
        self.items.append(item)

    def append_front(self, item):
        self.items.insert(0, item)

    def pop_front(self):
        return self.items.pop(0)

    def pop_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    deque_list = Deque()
    print(deque_list.isEmpty())
    deque_list.append_rear(8)
    deque_list.append_rear(5)
    deque_list.append_front(7)
    deque_list.append_front(10)
    print(deque_list.size())
    print(deque_list.isEmpty())
    deque_list.append_rear(11)
    print(deque_list.pop_rear())
    print(deque_list.pop_front())
    deque_list.append_front(55)
    deque_list.append_rear(45)
    print(deque_list.items)
