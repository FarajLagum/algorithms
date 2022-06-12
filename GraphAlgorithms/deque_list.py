# Deque implementaion in python with lists

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert_rear(self, item):
        self.items.append(item)

    def insert_front(self, item):
        self.items.insert(0, item)

    def remove__front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main":
    deque_list = Deque()
    print(deque_list.isEmpty())
    deque_list.insert_rear(8)
    deque_list.insert_rear(5)
    deque_list.insert_front(7)
    deque_list.insert_front(10)
    print(deque_list.size())
    print(deque_list.isEmpty())
    deque_list.insert_rear(11)
    print(deque_list.remove_rear())
    print(deque_list.remove_front())
    deque_list.insert_front(55)
    deque_list.insert_rear(45)
    print(deque_list.items)
