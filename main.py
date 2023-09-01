import random

class Board:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__cells = []
    
    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        self.__cells = cells

def pretty_print(board : Board):
    print('-' * (board.width + 2))
    for line in board.cells:
        print('|', end="")
        for val in line:
            if val == 1:
                print('■', end="")
            else:
                print(' ', end="")
        print('|')
    print('-' * (board.width + 2))

def random_state(width: int, height: int) -> Board:
    board = Board(width, height)
    cells = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
    board.cells = cells
    return board

pretty_print(random_state(16, 8))
