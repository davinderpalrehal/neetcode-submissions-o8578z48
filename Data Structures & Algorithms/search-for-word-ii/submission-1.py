class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dictionary = Trie()
        for w in words:
            dictionary.insert(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, visited, word):
            if (r, c) in visited:
                return
            
            if node.isWord:
                res.add(word)
            
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in node.children:
                    dfs(nr, nc, node.children[board[nr][nc]], visited, word + board[nr][nc])
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in dictionary.root.children:
                    dfs(r, c, dictionary.root.children[board[r][c]], set(), board[r][c])
        
        return list(res)