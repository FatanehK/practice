from collections import defaultdict

class TrieNode:
    def __init__(self):
        # nodes store a map to child node
        self.map = defaultdict(TrieNode)

        # isEndOfWord is true if the node
        # represents end of a word
        self.is_end_of_word = False

class Trie:
    # function to make a new trie
    def __init__(self):
        self.root = TrieNode()

    # function to insert in trie
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # if char not in node.map:
            #     node = node.map[TrieNode()]
            # make a new node if there is no path
            node = node.map[char]
        node.is_end_of_word = True

    # function to search in trie
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.map:
                return False
            node = node.map[char]
        return node.is_end_of_word

# Driver function
if __name__ == '__main__':
    # create a new Trie
    root = Trie()

    root.insert('geeks')
    print(root.search('geeks'), end=' ')

    root.insert('for')
    print(root.search('for'), end=' ')

    root.insert('geekk')
    print(root.search('geekk'), end=' ')

    root.insert('gee')
    print(root.search('gee'), end=' ')

    root.insert('science')
    print(root.search('science'))

