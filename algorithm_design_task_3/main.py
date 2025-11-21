import FreeSimpleGUI as sg
from game import TicTacToe3D
from ai import AI
from gui import GUI

def main():
    game = TicTacToe3D()
    ai = AI(game)
    gui = GUI()
    window = gui.create_window()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'New Game':
            game.reset()
            gui.update_board(game.board)
            continue

        if isinstance(event, int) and 0 <= event < 64:
            if game.current_winner:
                continue
            if game.make_move(event, 1):
                gui.update_board(game.board)
                
                winner = game.check_win()
                if winner:
                    game.current_winner = winner
                    gui.show_message("You Win!")
                    continue
                
                if game.is_full():
                    gui.show_message("Draw!")
                    continue

                window.perform_long_operation(lambda: ai_move_wrapper(game, ai, values['-DIFFICULTY-'], window), '-AI-DONE-')
            else:
                pass

        if event == '-AI-DONE-':
            move_idx = values[event]
            if move_idx is not None:
                game.make_move(move_idx, -1)
                gui.update_board(game.board)
                
                winner = game.check_win()
                if winner:
                    game.current_winner = winner
                    gui.show_message("Computer Wins!")
                elif game.is_full():
                    gui.show_message("Draw!")

def ai_move_wrapper(game, ai, difficulty, window):
    return ai.get_best_move(game.board[:], difficulty)

if __name__ == "__main__":
    main()
