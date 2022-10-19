class UnionFind:
    def __init__(self, dic):
        self.dic = dic
        self.parent = []
        self.rank = [1] * len(dic)
        self.num_of_components = len(dic)

    def building(self):
        size = self.num_of_components
        self.parent = [i for i in range(size)]

    def root_finder(self, current_node):
        root = current_node
        while root != self.parent[root]:
            root = self.parent[root]

        while current_node != root:
            next_node = self.parent[current_node]
            self.parent[current_node] = root
            current_node = next_node
        return root

    def whos_my_mamma(self, node):
        root = node
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union_find(self, p, q):
        root_p, root_q = self.root_finder(p), self.root_finder(q)

        if root_p != root_q:
            if self.rank[root_p] < self.rank[root_q]:
                self.rank[root_q] += self.rank[root_p]
                self.rank[root_p] = 0
                self.parent[root_p] = root_q
            else:
                self.rank[root_p] += self.rank[root_q]
                self.rank[root_q] = 0
                self.parent[root_q] = root_p
            self.num_of_components -= 1


#     Test Case:
#     ----------
#     dic = {'E': 0, 'F': 1, 'I': 2, 'D': 3, 'C': 4, 'A': 5, 'J': 6, 'L': 7, 'G': 8, 'K': 9, 'B': 10, 'H': 11}
#     sets = [['C', 'K'], ['F', 'E'], ['A', 'J'], ['A', 'B'], ['C', 'D'], ['D', 'I'], ['L', 'F'], ['C', 'A'], ['A', 'B'],
#             ['H', 'G'], ['H', 'F'], ['H', 'B']]

if __name__ == '__main__':
    sets = [['C', 'K'], ['F', 'E'], ['A', 'J'], ['A', 'B'], ['C', 'D'], ['D', 'I'], ['L', 'F'], ['C', 'A'], ['A', 'B'],
            ['H', 'G'], ['H', 'F'], ['H', 'B']]
    record, counter = {}, 0
    for i, j in sets:
        if i not in record:
            record[i] = counter
            counter += 1
        if j not in record:
            record[j] = counter
            counter += 1
    obj = UnionFind(record)
    obj.building()
    for p, q in sets:
        obj.union_find(record[p], record[q])
    print(f'Parents: {obj.parent}')
    print(f'Root Rank: {obj.rank}')
    print(f'Number of Sets: {obj.num_of_components}')
    print(f'Parent of node A: {obj.whos_my_mamma(record["A"])}')
