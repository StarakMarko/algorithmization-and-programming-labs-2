class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root

        for i in word:
            if i not in current_node.children:
                current_node.children[i] = Node()
            current_node = current_node.children[i]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root

        for i in word:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        return current_node.is_end_of_word

    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False
            current_node.is_end_of_word = False
            return len(current_node.children) == 0

        c = word[index]
        node = current_node.children.get(c)

        if node is None:
            return False

        delete_curent_node = self._delete(node, word, index + 1)

        if delete_curent_node:
            current_node.children.pop(c)
            return len(current_node.children) == 0 and not current_node.is_end_of_word

    def delete(self, word):
        self._delete(self.root, word, 0)

    def starts_with(self, prefix):
        words = []
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return words
            current_node = current_node.children[char]

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append("".join(path))

            for c, child_node in current_node.children.items():
                _dfs(child_node, path + [c])

        _dfs(current_node, list(prefix))

        return words


def build_trie(filename):
    trie = Trie()

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            pattern = line.strip()
            if pattern:
                trie.insert(pattern)

    return trie
