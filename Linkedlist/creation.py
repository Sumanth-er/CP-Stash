class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class llist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


my_list = llist()
my_list.append("a")
my_list.append("b")
my_list.display()
