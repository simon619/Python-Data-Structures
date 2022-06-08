class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None

    def __append__(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def __print__(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            if current_node.next is self.head:
                break
            current_node = current_node.next

    def __prepend__(self, data):
        current_node = self.head
        new_node = Node(data)
        prev = None
        while current_node:
            if current_node.next == self.head:
                prev = current_node
                break
            current_node = current_node.next
        self.head = new_node
        self.head.next = prev.next
        prev.next = self.head

    def __remove__(self, element):
        if self.head.data == element:
            prev = None
            current_node = self.head
            while current_node:
                if current_node.next is self.head:
                    prev = current_node
                    break
                current_node = current_node.next

            self.head = self.head.next
            prev.next = self.head

        else:
            current_node = self.head
            while current_node:
                if current_node.next is self.head:
                    break
                if current_node.next.data == element:
                    current_node.next = current_node.next.next
                current_node = current_node.next

    def __split_linklist__(self, pointer):
        count = 1
        current_node = self.head
        prev = None
        new_head = None
        temp = None
        while current_node:
            if current_node.next is self.head:
                break
            if count == pointer:
                new_head = current_node
                temp = prev
            prev = current_node
            count += 1
            current_node = current_node.next

        current_node.next = new_head
        temp.next = self.head
        print('Other Half')
        current_node2 = new_head
        while current_node2:
            print(current_node2.data)
            if current_node2.next is new_head:
                break
            current_node2 = current_node2.next

    def __is_circular__(self):
        current_node = self.head
        while current_node:
            if current_node.next is self.head:
                return True
            if current_node.next is None:
                return False
            current_node = current_node.next


if __name__ == '__main__':
    list1 = [1, 5, 6, 2, 8]
    cir_link_list1 = CircularLinkList()
    for i in list1:
        cir_link_list1.__append__(i)
    cir_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Prepending')
    cir_link_list1.__prepend__('S')
    cir_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Removing')
    cir_link_list1.__remove__(8)
    cir_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Spliting')
    list2 = [1, 5, 6, 2, 8, 4, 9, 50, 25, 19, 7]
    cir_link_list2 = CircularLinkList()
    for i in list2:
        cir_link_list2.__append__(i)
    cir_link_list2.__print__()
    cir_link_list2.__split_linklist__(4)  # Splite from 4th index
    print('Spliting Begins')
    cir_link_list2.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Is Circular?')
    x = cir_link_list2.__is_circular__()
    print(x)
