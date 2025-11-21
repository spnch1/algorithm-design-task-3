import random
import math

class AI:
    def __init__(self, game):
        self.game = game
        self.centers = [21, 22, 25, 26, 37, 38, 41, 42]

    def get_best_move(self, board, difficulty):
        valid_moves = [i for i, x in enumerate(board) if x == 0]
        if not valid_moves:
            return None

        if difficulty == 'Easy':
            winning_move = self.find_winning_move(board, -1, valid_moves)
            if winning_move is not None: return winning_move
            
            if random.random() < 0.4:
                blocking_move = self.find_winning_move(board, 1, valid_moves)
                if blocking_move is not None: return blocking_move
            
            return random.choice(valid_moves)
        
        elif difficulty == 'Medium':
            winning_move = self.find_winning_move(board, -1, valid_moves)
            if winning_move is not None: return winning_move
            
            blocking_move = self.find_winning_move(board, 1, valid_moves)
            if blocking_move is not None: return blocking_move

            center_moves = [m for m in valid_moves if m in self.centers]
            if center_moves:
                return random.choice(center_moves)
            
            return random.choice(valid_moves)

        elif difficulty == 'Hard':
            winning_move = self.find_winning_move(board, -1, valid_moves)
            if winning_move is not None: return winning_move
            
            blocking_move = self.find_winning_move(board, 1, valid_moves)
            if blocking_move is not None: return blocking_move

            center_moves = [m for m in valid_moves if m in self.centers]
            if center_moves:
                return random.choice(center_moves)
            
            return random.choice(valid_moves)

            ordered_moves = self.order_moves(board, valid_moves)
            
            best_score = -math.inf
            best_move = ordered_moves[0]
            
            for move in ordered_moves:
                board[move] = -1
                score = self.minimax(board, 2, -math.inf, math.inf, False)
                board[move] = 0
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        
        return random.choice(valid_moves)

    def find_winning_move(self, board, player, valid_moves):
        for move in valid_moves:
            board[move] = player
            if self.check_win_fast(board, player):
                board[move] = 0
                return move
            board[move] = 0
        return None

    def check_win_fast(self, board, player):
        for line in self.game.winning_lines:
            if all(board[i] == player for i in line):
                return True
        return False

    def order_moves(self, board, moves):
        def score_move(move):
            score = 0
            if move in self.centers:
                score += 10
            return score
        
        return sorted(moves, key=score_move, reverse=True)

    def evaluate(self, board):
        score = 0
        for line in self.game.winning_lines:
            values = [board[i] for i in line]
            x_count = values.count(1)
            o_count = values.count(-1)
            
            if x_count > 0 and o_count > 0:
                continue
            
            if o_count > 0:
                if o_count == 4: return 10000
                if o_count == 3: score += 100
                if o_count == 2: score += 10
                if o_count == 1: score += 1
            
            if x_count > 0:
                if x_count == 4: return -10000
                if x_count == 3: score -= 100
                if x_count == 2: score -= 10
                if x_count == 1: score -= 1
        
        return score

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        current_eval = self.evaluate(board)
        if abs(current_eval) >= 5000:
            return current_eval
        
        if depth == 0 or 0 not in board:
            return current_eval

        valid_moves = [i for i, x in enumerate(board) if x == 0]
        
        if maximizing_player:
            max_eval = -math.inf
            for move in valid_moves:
                board[move] = -1
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                board[move] = 0
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in valid_moves:
                board[move] = 1
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board[move] = 0
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
