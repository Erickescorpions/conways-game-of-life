import random
from enum import Enum

class CellState(Enum):
    DEAD = 0
    ALIVE = 1

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
                print('◼', end="")
            else:
                print(' ', end="")
        print('|')
    print('-' * (board.width + 2))

def random_state(width: int, height: int) -> list:
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]

'''
Exiten 4 reglas:
- si una celula tiene solo 1 o ningun vecino, muere por falta de celulas. 
- si una celula viva tiene 2 o 3 vecinos, se mantiene vivita y coleando. 
- si una celula tiene mas de 3 vecinos, muere por sobrepoblacion.
- si una celula muerta tiene exactamente 3 vecinos vivos, vuelve a la vida. 
'''
def next_board_state(cells) -> list:
    '''
    vamos a recorrer todas las celulas una por una
    vamos a realizar un calculo que nos otorgue las celulas vecinas
    celulas = 
    [   [1, 0, 0]
        [0, 1, 0]
        [0, 0, 1]    ]

    tomando la matriz de arriba, podemos ver que para calcular los vecinos de
    la celula en la posicion celulas [0, 0], es necesario revisar todas las
    coordenadas que se encuentran a su alrededor y que son positivas.
    [0, 1], [1, 0], [1, 1].
    Otro ejemplo, para la celula [1, 1], se debe de revisar [0, 0], [0, 1], 
    [0, 2], [1, 0], [1, 2], [2, 0], [2, 1] y [2, 2]
    Podemos observar que son 9 posibles celulas vecinas, las cuales se calculan 
    restando o sumando una unidad en las coordenadas dependiendo el caso. 

    '''
    height = len(cells)
    width = len(cells[0])

    new_cells = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            # de esta manera vamos a dar una pasada por todo el tablero
            state = cells[i][j]
            neighbors_alive = 0

            # revisamos todos los vecinos
            # [i - 1, j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                if cells[i - 1][j - 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i - 1, j]
            if i - 1 >= 0:
                if cells[i - 1][j] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i - 1, j + 1]
            if i - 1 >= 0 and j + 1 < width:
                if cells[i - 1][j + 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i, j - 1]
            if j - 1 >= 0:
                if cells[i][j - 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i, j + 1]
            if j + 1 < width:
                if cells[i][j + 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i + 1, j - 1]
            if i + 1 < height and j - 1 >= 0:
                if cells[i + 1][j - 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i + 1, j]
            if i + 1 < height:
                if cells[i + 1][j] == 1:
                    neighbors_alive = neighbors_alive + 1

            # [i + 1, j + 1]
            if i + 1 < height and j + 1 < width:
                if cells[i + 1][j + 1] == 1:
                    neighbors_alive = neighbors_alive + 1

            # aplicamos las reglas
            if state == 1:
                if neighbors_alive <= 1 or neighbors_alive > 3:
                    new_cells[i][j] = 0
                else:
                    new_cells[i][j] = 1
            elif state == 0:
                if neighbors_alive == 3:
                    new_cells[i][j] = 1
                else:
                    new_cells[i][j] = 0
            
    return new_cells

if __name__ == '__main__':
    width = 38
    height = 20
    # width = 5
    # height = 5
    board = Board(width, height)

    #board.cells = random_state(width, height)
    board.cells = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # board.cells = [
    #     [0,0,0,0,0],
    #     [0,0,0,0,0],
    #     [0,1,1,1,0],
    #     [0,0,0,0,0],
    #     [0,0,0,0,0]
    # ]

    # for i in range(1):
    #     pretty_print(board)
    #     board.cells = next_board_state(board.cells)

    while True:
        pretty_print(board)
        board.cells = next_board_state(board.cells)
