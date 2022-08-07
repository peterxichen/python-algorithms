# Add and Search Words Data Structure
# Add/Search using trie, if wildcard (".") then search all subnodes recursively
# time: O(n) add/search, space: O(n) add, O(1) search
# For searching "dotted" words, time: O(num_keys*26^key_length), space: O(key_length)
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if cur.get(c) is None:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#'

    def search(self, word: str) -> bool:
        def searchTrie(word, cur) -> bool:
            for i, c in enumerate(word): # index + char
                if c in cur: # c found, iter next
                    cur = cur[c]
                else:
                    if c == '.': # check all subnodes at level
                        for subnode in cur:
                            if subnode != '#' and searchTrie(word[i+1:], cur[subnode]):
                                return True
                    return False # no subnodes give answer
            return cur.get('#') == '#'
        return searchTrie(word, self.trie)    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
