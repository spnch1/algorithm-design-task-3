import FreeSimpleGUI as sg

class GUI:
    def __init__(self):
        self.window = None
        self.buttons = []

    def create_layout(self):
        sg.theme('DarkBlue3')
        
        layers = []
        for z in range(4):
            layer_layout = []
            layer_layout.append([sg.Text(f'Layer {z+1}', justification='center', expand_x=True)])
            for y in range(4):
                row = []
                for x in range(4):
                    idx = x * 16 + y * 4 + z
                    btn = sg.Button('', size=(4, 2), key=idx, button_color=('white', 'gray'))
                    row.append(btn)
                    self.buttons.append(btn)
                layer_layout.append(row)
            layers.append(sg.Frame(f'', layer_layout, element_justification='center'))

        controls = [
            [sg.Text('Difficulty:', font=('Helvetica', 12)), 
             sg.Combo(['Easy', 'Medium', 'Hard'], default_value='Medium', key='-DIFFICULTY-', readonly=True, size=(10,1))],
            [sg.Button('New Game', size=(10, 1)), sg.Button('Exit', size=(10, 1))],
            [sg.Text('Player: X (Blue) | Computer: O (Red)', font=('Helvetica', 10))]
        ]

        layout = [
            [sg.Text('3D 4x4x4 Noughts and Crosses', font=('Helvetica', 16), justification='center', expand_x=True)],
            [sg.Column([[layers[0], layers[1], layers[2], layers[3]]], element_justification='center')],
            [sg.Column(controls, element_justification='center')]
        ]
        
        return layout

    def create_window(self):
        self.window = sg.Window('3D Tic-Tac-Toe', self.create_layout(), finalize=True)
        return self.window

    def update_board(self, board):
        for i, val in enumerate(board):
            if val == 1:
                self.window[i].update(text='X', button_color=('white', 'blue'))
            elif val == -1:
                self.window[i].update(text='O', button_color=('white', 'red'))
            else:
                self.window[i].update(text='', button_color=('white', 'gray'))

    def show_message(self, message):
        sg.popup(message, title='Game Over')

    def close(self):
        if self.window:
            self.window.close()
