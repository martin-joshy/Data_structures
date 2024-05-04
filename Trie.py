class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    
if __name__ == "__main__":
    trie = Trie()

    # Insert words
    words = ["apple", "banana", "grape", "grapefruit", "mango"]
    for word in words:
        trie.insert(word)

    # Search for some words
    print(trie.search("apple"))  # True
    print(trie.search("grape"))  # True
    print(trie.search("orange"))  # False

    # Check if certain prefixes exist
    print(trie.startsWith("app"))  # True
    print(trie.startsWith("man"))  # True
    print(trie.startsWith("ora"))  # False


    # Search for the deleted word
    print(trie.search("apple"))  # False
