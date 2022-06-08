class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkList:
    def __init__(self):
        self.head = None

    def __print__(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def __append__(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def __prepend__(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def __add_a_new_node__(self, prev_node_data, data):
        current_node = self.head
        new_node = Node(data)
        while current_node:
            if current_node.data is prev_node_data:
                temp = current_node.next
                current_node.next = new_node
                new_node.next = temp
            current_node = current_node.next

    def __delete_a_node__(self, DATA):
        current_node = self.head
        if current_node.data is DATA:
            self.head = current_node.next  # To remove the head
        else:
            while current_node.next:
                if current_node.next.data is DATA:
                    if current_node.next.next is not None:  # Removes Everything between head and tail
                        current_node.next = current_node.next.next
                    elif current_node.next.next is None:  # To remove tail
                        current_node.next = None
                        break
                current_node = current_node.next

    def __counting_length_recursively__(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.__counting_length_recursively__(node.next)

    def __swaping_nodes__(self, data1, data2):
        self.list = []
        current_node = self.head
        if current_node.data is data1:
            head_instance = current_node.next
            while current_node.next:
                if current_node.next.data is data2:
                    if current_node.next.next is not None:
                        temp1 = current_node.next
                        temp2 = current_node.next.next
                        current_node.next = self.head
                        current_node.next.next = temp2
                        self.head = temp1
                        self.head.next = head_instance
                    if current_node.next.next is None:
                        temp = current_node.next
                        current_node.next = self.head
                        current_node.next.next = None
                        temp.next = head_instance
                        self.head = temp
                        break
                current_node = current_node.next

        if current_node.data is data2:
            head_instance = current_node.next
            while current_node.next:
                if current_node.next.data is data1:
                    if current_node.next.next is not None:
                        temp1 = current_node.next
                        temp2 = current_node.next.next
                        current_node.next = self.head
                        current_node.next.next = temp2
                        self.head = temp1
                        self.head.next = head_instance
                    if current_node.next.next is None:
                        temp = current_node.next
                        current_node.next = self.head
                        current_node.next.next = None
                        temp.next = head_instance
                        self.head = temp
                        break
                current_node = current_node.next
        else:
            while current_node.next:
                if current_node.next.data is data1 or current_node.next.data is data2:
                    self.list.append(current_node)
                current_node = current_node.next

            if self.list[1].next.next is not None:
                temp1 = self.list[0].next.next
                temp2 = self.list[1].next.next
                temp3 = self.list[0].next
                self.list[0].next = self.list[1].next
                self.list[0].next.next = temp1
                self.list[1].next = temp3
                self.list[1].next.next = temp2

            elif self.list[1].next.next is None:
                temp1 = self.list[0].next.next
                temp2 = self.list[0].next
                self.list[0].next = self.list[1].next
                self.list[0].next.next = temp1
                self.list[1].next = temp2
                self.list[1].next.next = None

    def __reverse__(self):
        def reverse(current, previous):
            if not current:
                return previous
            else:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

                return reverse(current, previous)

        self.head = reverse(self.head, None)

    def __remove_duplicate__(self):
        current_node = self.head
        dic = {}
        prev = None
        record = []
        while current_node:
            if current_node.data in dic:
                dic[current_node.data] = 2
                record.append(prev)
            else:
                dic[current_node.data] = 1
            prev = current_node
            current_node = current_node.next
        print(record[0].data)
        print(record[1].data)
        for i in record:
            if i.next.next:
                i.next = i.next.next
            else:
                i.next = None

    def __merge__(self, linklist2):
        len1 = self.__counting_length_recursively__(self.head)
        len2 = self.__counting_length_recursively__(linklist2.head)
        print(f'Length of 1st Link List is: {len1}')
        print(f'Length of 2nd Link List is: {len2}')
        current_node1 = self.head
        current_node2 = linklist2.head
        self.head = None
        current_node = None
        while current_node2 and current_node1:
            if current_node1.data < current_node2.data:
                if not self.head:
                    self.head = current_node1
                    current_node = self.head
                else:
                    current_node.next = current_node1
                    current_node = current_node.next
                current_node1 = current_node1.next
            else:
                if not self.head:
                    self.head = current_node2
                    current_node = self.head
                else:
                    current_node.next = current_node2
                    current_node = current_node.next
                current_node2 = current_node2.next
        while current_node1:
            current_node.next = current_node1
            current_node1 = current_node1.next
        while current_node2:
            current_node.next = current_node2
            current_node2 = current_node2.next

    def __rotation__(self, num):
        temp_node = self.head
        current_node = self.head
        count = 0
        self.head = None
        prev = None
        while current_node:
            if count is num:
                self.head = current_node
                prev.next = None
            count += 1
            prev = current_node
            current_node = current_node.next

        prev.next = temp_node

    def __is_singly__(self):
        current_node = self.head
        while current_node:
            if current_node.next is self.head:
                return False
            if current_node.next is None:
                return True
            current_node = current_node.next


if __name__ == '__main__':
    link_list0 = SinglyLinkList()
    print('Printing the LinkList')
    link_list0.__append__('A')
    link_list0.__append__('B')
    link_list0.__append__('C')
    link_list0.__append__('D')
    link_list0.__append__('F')
    link_list0.__print__()

    print('Printing the LinkList After Prepend')
    link_list0.__prepend__('S')
    link_list0.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Printing the LinkList After Adding A New Node')
    link_list0.__add_a_new_node__('D', 'E')
    link_list0.__print__()

    print('Printing the LinkList After Adding T')
    link_list0.__add_a_new_node__('D', 'T')
    link_list0.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Printing the LinkList After Deleting')
    link_list0.__delete_a_node__('T')
    link_list0.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Counting Number of Nodes')
    print(link_list0.__counting_length_recursively__(link_list0.head))
    print('-----------------------------------------------------------------------------------')
    print('Swaping The Elements')
    link_list0.__swaping_nodes__('F', 'A')
    link_list0.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Reverse The LinkList')
    link_list0.__reverse__()
    link_list0.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Merging Two LinkList')
    list1 = [1, 2, 6, 9, 20, 25]
    list2 = [3, 5, 7, 10, 19, 24]
    link_list1 = SinglyLinkList()
    for i in list1:
        link_list1.__append__(i)
    link_list1.__print__()
    link_list2 = SinglyLinkList()
    for i in list2:
        link_list2.__append__(i)
    link_list2.__print__()
    print('Merge Begins')
    link_list1.__merge__(link_list2)
    link_list1.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Remove Duplicate')
    list3 = [1, 2, 3, 4, 5, 7, 5, 9, 2, 10, 10, 15]
    link_list3 = SinglyLinkList()
    for i in list3:
        link_list3.__append__(i)
    print('Previous List')
    link_list3.__print__()
    print('After Removing')
    link_list3.__remove_duplicate__()
    link_list3.__print__()
    print('-----------------------------------------------------------------------------------')
    print('Left Rotation')
    list4 = [1, 2, 3, 4, 5, 7, 51, 60]
    link_list4 = SinglyLinkList()
    for i in list4:
        link_list4.__append__(i)
    link_list4.__print__()
    print('Rotation Begins')
    link_list4.__rotation__(3)
    link_list4.__print__()
    print('-----------------------------------------------------------------------------------')
    x = link_list4.__is_singly__()
    print(x)
