class TicTacToe3D:
    def __init__(self):
        self.board = [0] * 64  # 0: empty, 1: player (X), -1: computer (O)
        self.winning_lines = self._generate_winning_lines()
        self.current_winner = None

    def _generate_winning_lines(self):
        lines = []
        
        def idx(x, y, z): # converts xyz to index
            return x * 16 + y * 4 + z

        for y in range(4):
            for z in range(4):
                lines.append([idx(x, y, z) for x in range(4)])

        for x in range(4):
            for z in range(4):
                lines.append([idx(x, y, z) for y in range(4)])
        for x in range(4):
            for y in range(4):
                lines.append([idx(x, y, z) for z in range(4)])

        for z in range(4):
            lines.append([idx(i, i, z) for i in range(4)])
            lines.append([idx(i, 3 - i, z) for i in range(4)])
        
        for y in range(4):
            lines.append([idx(i, y, i) for i in range(4)])
            lines.append([idx(i, y, 3 - i) for i in range(4)])
        for x in range(4):
            lines.append([idx(x, i, i) for i in range(4)])
            lines.append([idx(x, i, 3 - i) for i in range(4)])

        lines.append([idx(i, i, i) for i in range(4)])
        lines.append([idx(i, i, 3 - i) for i in range(4)])
        lines.append([idx(i, 3 - i, i) for i in range(4)])
        lines.append([idx(i, 3 - i, 3 - i) for i in range(4)])

        return lines

    def check_win(self):
        for line in self.winning_lines:
            values = [self.board[i] for i in line]
            if all(v == 1 for v in values):
                return 1
            if all(v == -1 for v in values):
                return -1
        return None

    def get_valid_moves(self):
        return [i for i, x in enumerate(self.board) if x == 0]

    def make_move(self, index, player):
        if self.board[index] == 0:
            self.board[index] = player
            return True
        return False

    def is_full(self):
        return 0 not in self.board

    def reset(self):
        self.board = [0] * 64
        self.current_winner = None
