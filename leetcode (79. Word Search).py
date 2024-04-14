class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board_cnt = Counter([ch for row in board for ch in row])
        word_cnt = Counter(word)
        
        # optimization 1
        for ch in word_cnt:
            if word_cnt[ch] > board_cnt[ch]:
                return False
        
        # optimization 2
        word = word if word_cnt[word[0]] < word_cnt[word[-1]] else word[::-1]
        
        m, n = len(board), len(board[0])
        
        def dfs(x, y, index):
            if board[x][y] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True
            
            board[x][y] = "#"
            for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                if 0 <= nx < m and 0 <= ny < n and dfs(nx, ny, index+1):
                    return True
            board[x][y] = word[index]
            
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False