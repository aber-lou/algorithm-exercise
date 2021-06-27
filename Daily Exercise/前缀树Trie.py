class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node


    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        
        node.isWord = True

    def search(self, word:str) -> bool:
        node = self.searchPrefix(word)
        print(node)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None