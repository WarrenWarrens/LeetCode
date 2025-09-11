class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[""] * 3 for _ in range(3)]
        count = 0
        for r, c in moves:
            if count % 2 == 0:
                board[r][c] = "X"
            else:
                board[r][c] = "O"
            count += 1


        for i in range(3):
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
                return "A" if board[i][0] == "X" else "B"
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
                return "A" if board[0][i] == "X" else "B"

            if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
                return "A" if board[0][0] == "X" else "B"
            if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
                return "A" if board[0][2] == "X" else "B"
        return "Draw" if len(moves) == 9 else "Pending"






