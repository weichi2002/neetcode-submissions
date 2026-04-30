class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.addWord(word)
        
        ROWS = len(board)
        COLS = len(board[0])
        res = path = set()

        def dfs(r, c, node, word):

            if (
                c < 0 or r < 0 or
                c == COLS or r == ROWS or
                (r, c) in path or
                board[r][c] not in node.children
            ):
                return

            path.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.isWord:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            path.remove((r,c))


        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)



            