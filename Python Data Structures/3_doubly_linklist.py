class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prex = None


class DoublyLinkList:
    def __init__(self):
        self.head = None

    def __append__(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.prev = None

        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None

    def __print__(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def __backward_print__(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev

    def __prepend__(self, data):
        new_node = Node(data)
        old_head = self.head
        self.head = new_node
        self.head.next = old_head
        old_head.prev = self.head

    def __add_a_node_after__(self, prev_node_data, data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data is prev_node_data:
                temp = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = temp
            current_node = current_node.next

    def __add_a_node_before__(self, before_node_data, data):
        current_node = self.head
        new_node = Node(data)
        while current_node:
            if current_node.data is before_node_data:
                temp = current_node.prev
                temp.next = new_node
                new_node.prev = temp
                new_node.next = current_node
                current_node.prev = new_node
            current_node = current_node.next

    def __delete__(self, data):
        current_node = self.head
        while current_node.next:
            if current_node is self.head and current_node.data is data:  # If data is 1st node
                self.head = self.head.next
                self.head.prev = None
            elif current_node.data is data:
                current_node.next.prev = current_node.prev  # If data is between 1st node and last node
                current_node.prev.next = current_node.next
            current_node = current_node.next
            if current_node.data is data:  # If data is the last node
                current_node.prev.next = None


if __name__ == '__main__':
    doub_link_list1 = DoublyLinkList()
    list1 = [1, 6, 7, 2, 5, 11]
    for i in list1:
        doub_link_list1.__append__(i)
    print('-----------------------------------------------------------------------------------')
    doub_link_list1.__print__()
    print("Backward Printing")
    doub_link_list1.__backward_print__()
    print('-----------------------------------------------------------------------------------')
    print('Prepend')
    doub_link_list1.__prepend__('S')
    doub_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Add a Node After a Node')
    doub_link_list1.__add_a_node_after__(11, 10)
    doub_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Add a Node Before a Node')
    doub_link_list1.__add_a_node_before__(10, 90)
    doub_link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Delete a Node')
    doub_link_list1.__print__()
    print('Delete Starts')
    doub_link_list1.__delete__(10)
    doub_link_list1.__print__()

