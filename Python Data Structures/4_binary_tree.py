import random


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __appending_nodes__(self):
        pointer = 0

        def build_the_tree(node, level, value):
            if level <= 3:
                if node is None:
                    node = Tree(value)
                    level += 1
                node.left = build_the_tree(node.left, level, 2 * value + 1)
                node.right = build_the_tree(node.right, level, 2 * value + 2)

            else:
                node = None
            return node

        self.root = build_the_tree(self.root, pointer, pointer)

    def __preorder_traversal__(self):
        current_node = self.root

        def __traversal__(node, traversal):
            if node:
                traversal += (str(node.data) + '->')
                traversal = __traversal__(node.left, traversal)
                traversal = __traversal__(node.right, traversal)
            return traversal

        result = __traversal__(current_node, '')
        return result

    def __inorder_traversal__(self):
        current_node = self.root

        def __traversal__(node, traversal):
            if node:
                traversal = __traversal__(node.left, traversal)
                traversal += (str(node.data) + '->')
                traversal = __traversal__(node.right, traversal)
            return traversal

        result = __traversal__(current_node, '')
        return result

    def __postorder_traversal__(self):
        current_node = self.root

        def __traversal__(node, traversal):
            if node:
                traversal = __traversal__(node.left, traversal)
                traversal = __traversal__(node.right, traversal)
                traversal += (str(node.data) + '->')
            return traversal

        result = __traversal__(current_node, '')
        return result

    def __noorder_traversal__(self):
        current_node = self.root
        q = [current_node]

        def __traversal__(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                if info.left:
                    q.append(info.left)
                if info.right:
                    q.append(info.right)
                traversal = __traversal__(q, traversal)
            return traversal

        result = __traversal__(q, '')
        return result

    def __reverse_traversal__(self):
        current_node = self.root
        que = [current_node]
        stack = []
        def __reverse__(qu, st):
            if que:
                while que:
                    node = qu.pop(0)
                    st.append(node)
                    if node.right:
                        qu.append(node.right)
                    if node.left:
                        qu.append(node.left)
                st = __reverse__(qu, st)
            return st

        def __print__(st, traversal):
            if st:
                traversal += str(st.pop().data) + '->'
                traversal = __print__(st, traversal)
            return traversal

        result = __reverse__(que, stack)
        traversed = __print__(result, '')
        return traversed

    def __calculate_the_level__(self):
        current_node = self.root
        def __calculation__(node):
            if node is None:
                return -1
            else:
                left = __calculation__(node.left)
                right = __calculation__(node.right)
            return 1 + max(left, right)

        depth = __calculation__(current_node)
        return depth

    def __print__(self):
        current_node = self.root
        prev = None
        while current_node:
            print(current_node.data)
            prev = current_node
            current_node = current_node.right
        prev.right = Tree(100)
        print(self.root.right.right.right.right.data)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.__appending_nodes__()
    print('Printing Randomly')
    tree.__print__()
    print('Preorder Traversal:')
    print(tree.__preorder_traversal__())
    print('Inorder Traversal:')
    print(tree.__inorder_traversal__())
    print('Postorder Traversal:')
    print(tree.__postorder_traversal__())
    print('Noorder Traversal:')
    print(tree.__noorder_traversal__())
    print('Reverse Traversal:')
    print(tree.__reverse_traversal__())
    print('Calculation the Depth of the Tree')
    x = tree.__calculate_the_level__()
    print(f'Depth: {x}')