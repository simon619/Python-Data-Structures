class TrieNode:

    def __init__(self):
        self.char_list = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = None

    def insert_trie(self, word):
        if not self.root:
            self.root = TrieNode()
        current_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) % 26
            print(index)

            if not current_node.char_list[index]:
                current_node.char_list[index] = TrieNode()
            current_node = current_node.char_list[index]

        current_node.is_end = True

    def search_word(self, word):
        if not self.root:
            return False
        current_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) % 26

            if not current_node.char_list[index]:
                return False
            current_node = current_node.char_list[index]
        return current_node.is_end


if __name__ == '__main__':
    obj = Trie()
    insert_list = ["apple", "simon"]
    search_list = ["apple", "ap", "ape", "simon"]
    for i in insert_list:
        obj.insert_trie(i)
    bol = [obj.search_word(i) for i in search_list]
    print(bol)


