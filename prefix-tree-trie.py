# Prefix Tree (trie)
# init trie as dict, key = char, value = new dict,
# search and insert by iterating through trie
# insert/search/prefix time: O(n)
# insert space: O(n), search/prefix space: O(1)

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if cur.get(c) is None:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#' # mark end of word

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if cur.get(c) is None:
                return False
            cur = cur[c]
        if cur.get('#'):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if cur.get(c) is None:
                return False
            cur =cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
